import pytest
from pathlib import Path
from src.parser import parse_seed_file, SeedParseError

def test_parse_basic_theme():
    """Test parsing a basic theme definition with type validation"""
    content = """
    theme basic {
        colors {
            primary: color(#000000)
            secondary: color(blue.500)
        }
        spacing {
            small: size(4px)
            medium: size(8px)
        }
    }
    """
    with Path("test_theme.seed").open("w") as f:
        f.write(content)
        
    result = parse_seed_file(Path("test_theme.seed"))
    
    assert "basic" in result
    assert result["basic"]["colors"]["primary"] == "color(#000000)"
    assert result["basic"]["colors"]["secondary"] == "color(blue.500)"
    assert result["basic"]["spacing"]["small"] == "size(4px)"
    
    Path("test_theme.seed").unlink()

def test_parse_nested_structure():
    """Test parsing nested structures with type validation"""
    content = """
    theme test {
        typography {
            fontFamily {
                base: font("Arial")
                heading: font("Helvetica")
            }
            size {
                base: size(16px)
                heading: size(24px)
            }
        }
    }
    """
    with Path("test_theme.seed").open("w") as f:
        f.write(content)
        
    result = parse_seed_file(Path("test_theme.seed"))
    
    assert result["test"]["typography"]["fontFamily"]["base"] == 'font("Arial")'
    assert result["test"]["typography"]["size"]["base"] == "size(16px)"
    
    Path("test_theme.seed").unlink()

def test_parse_value_types():
    """Test parsing and validating different value types"""
    content = """
    theme types {
        values {
            string_val: string("text")
            number_val: number(42)
            float_val: number(3.14)
            true_val: boolean(true)
            false_val: boolean(false)
            color_val: color(#ff0000)
            size_val: size(16px)
            token_val: color(blue.500)
        }
    }
    """
    with Path("test_theme.seed").open("w") as f:
        f.write(content)
        
    result = parse_seed_file(Path("test_theme.seed"))
    values = result["types"]["values"]
    
    assert values["string_val"] == 'string("text")'
    assert values["number_val"] == "number(42)"
    assert values["float_val"] == "number(3.14)"
    assert values["true_val"] == "boolean(true)"
    assert values["false_val"] == "boolean(false)"
    assert values["color_val"] == "color(#ff0000)"
    assert values["size_val"] == "size(16px)"
    assert values["token_val"] == "color(blue.500)"
    
    Path("test_theme.seed").unlink()

def test_parse_invalid_types():
    """Test handling of invalid type declarations according to spec"""
    content = """
    theme invalid {
        colors {
            // Invalid: Missing explicit type declaration
            primary: "#000000"
            
            // Invalid: Color token doesn't exist
            secondary: color(invalid.500)
            
            // Invalid: Wrong type format
            tertiary: rgb(invalid)
            
            // Invalid: Missing unit in size
            spacing: size(4)
            
            // Invalid: Wrong enum value
            variant: enum(invalid)
        }
    }
    """
    with Path("test_theme.seed").open("w") as f:
        f.write(content)
        
    with pytest.raises(SeedParseError) as exc_info:
        parse_seed_file(Path("test_theme.seed"))
    
    error = str(exc_info.value)
    assert "Missing explicit type declaration" in error
    assert "Invalid color token" in error
    assert "Invalid size format" in error
    
    Path("test_theme.seed").unlink()

def test_parse_invalid_syntax():
    """Test handling of invalid syntax"""
    content = """
    theme invalid {
        button {
            // Invalid nesting
            hover.background: color(blue.500)
            
            // Missing closing brace
            primary {
                background: color(blue.500)
    """
    with Path("test_theme.seed").open("w") as f:
        f.write(content)
        
    with pytest.raises(SeedParseError):
        parse_seed_file(Path("test_theme.seed"))
    
    Path("test_theme.seed").unlink()

def test_parse_schema_validation():
    """Test component schema validation according to spec"""
    content = """
    // Define button schema
    schema Button {
        required {
            background: color
            text: color
            padding: spacing
        }
        optional {
            border: border
            hover: {
                background: color
                text: color
            }
        }
    }
    
    theme test {
        button {
            // Missing required padding property
            background: color(blue.500)
            text: color(white)
            
            // Invalid: Unknown property
            shadow: size(2px)
            
            // Invalid: Wrong type for border
            border: color(black)
            
            // Invalid hover structure
            hover: color(blue.600)
        }
    }
    """
    with Path("test_theme.seed").open("w") as f:
        f.write(content)
        
    with pytest.raises(SeedParseError) as exc_info:
        parse_seed_file(Path("test_theme.seed"))
    
    error = str(exc_info.value)
    assert "Missing required property: padding" in error
    assert "Unknown property: shadow" in error
    assert "Invalid type for property: border" in error
    assert "Invalid hover structure" in error
    
    Path("test_theme.seed").unlink()

def test_circular_imports():
    """Test detection of circular imports"""
    # Create theme_a.seed
    with Path("theme_a.seed").open("w") as f:
        f.write("""
        import "theme_b.seed"
        theme a extends b {
            button {
                primary {
                    background: color(red.500)
                }
            }
        }
        """)
    
    # Create theme_b.seed
    with Path("theme_b.seed").open("w") as f:
        f.write("""
        import "theme_a.seed"
        theme b extends a {
            button {
                primary {
                    background: color(blue.500)
                }
            }
        }
        """)
    
    with pytest.raises(SeedParseError, match=r".*Circular import detected.*"):
        parse_seed_file(Path("theme_a.seed"))
    
    Path("theme_a.seed").unlink()
    Path("theme_b.seed").unlink()

def test_type_validation():
    """Test type validation rules according to spec"""
    content = """
    theme test {
        typography {
            // String validation
            title: string {
                min: 2
                max: 50
                pattern: "[A-Za-z ]+"
            }
            
            // Number validation
            fontSize: number {
                min: 12
                max: 96
                integer: true
                positive: true
            }
            
            // Size validation
            spacing: size {
                type: px
                value: 16
            }
            
            // Color validation
            textColor: color {
                type: hex
                value: "#000000"
            }
            
            // Font validation
            font: {
                family: string("Inter")
                size: size(16px)
                weight: number(600)
                lineHeight: number(1.5)
            }
        }
    }
    """
    with Path("test_theme.seed").open("w") as f:
        f.write(content)
    
    result = parse_seed_file(Path("test_theme.seed"))
    
    assert "typography" in result["test"]
    assert result["test"]["typography"]["fontSize"]["value"] == 16
    assert result["test"]["typography"]["textColor"]["value"] == "#000000"
    
    Path("test_theme.seed").unlink()

def test_responsive_values():
    """Test responsive value definitions according to spec"""
    content = """
    theme test {
        typography {
            heading {
                // Responsive size values
                size: {
                    base: size(24px)
                    sm: size(20px)
                    md: size(28px)
                    lg: size(32px)
                }
                // Responsive line height
                lineHeight: {
                    base: number(1.2)
                    sm: number(1.1)
                    lg: number(1.3)
                }
            }
        }
    }
    """
    with Path("test_theme.seed").open("w") as f:
        f.write(content)
    
    result = parse_seed_file(Path("test_theme.seed"))
    heading = result["test"]["typography"]["heading"]
    
    assert heading["size"]["base"] == "size(24px)"
    assert heading["size"]["sm"] == "size(20px)"
    assert heading["size"]["lg"] == "size(32px)"
    assert heading["lineHeight"]["base"] == "number(1.2)"
    
    Path("test_theme.seed").unlink()

def test_theme_composition():
    """Test theme composition and inheritance"""
    # Create base theme
    with Path("base.seed").open("w") as f:
        f.write("""
        theme base {
            colors {
                primary: color(#0066cc)
                secondary: color(#666666)
            }
            typography {
                body: {
                    size: size(16px)
                    lineHeight: number(1.5)
                }
            }
        }
        """)
    
    # Create extended theme
    with Path("custom.seed").open("w") as f:
        f.write("""
        import "./base.seed"
        
        theme custom extends base {
            colors {
                // Override primary color
                primary: color(#ff0000)
                // Add new color
                accent: color(#00ff00)
            }
            // Keep typography from base
        }
        """)
    
    result = parse_seed_file(Path("custom.seed"))
    
    assert result["custom"]["colors"]["primary"] == "color(#ff0000)"
    assert result["custom"]["colors"]["secondary"] == "color(#666666)"
    assert result["custom"]["colors"]["accent"] == "color(#00ff00)"
    assert result["custom"]["typography"]["body"]["size"] == "size(16px)"
    
    Path("base.seed").unlink()
    Path("custom.seed").unlink()

def test_invalid_theme_composition():
    """Test invalid theme composition scenarios"""
    # Create theme with invalid extension
    content = """
    theme invalid extends nonexistent {
        colors {
            primary: color(#ff0000)
        }
    }
    """
    with Path("test_theme.seed").open("w") as f:
        f.write(content)
    
    with pytest.raises(SeedParseError, match=r".*Unknown base theme.*"):
        parse_seed_file(Path("test_theme.seed"))
    
    Path("test_theme.seed").unlink()
