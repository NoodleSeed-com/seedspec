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
    """Test handling of invalid type declarations"""
    content = """
    theme invalid {
        colors {
            // Missing type declaration
            primary: "#000000"
            // Invalid color value
            secondary: color(invalid)
        }
    }
    """
    with Path("test_theme.seed").open("w") as f:
        f.write(content)
        
    with pytest.raises(SeedParseError, match=r".*Missing type declaration.*"):
        parse_seed_file(Path("test_theme.seed"))
    
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
    """Test component schema validation"""
    content = """
    // Define button schema
    schema Button {
        required {
            background: color
            text: color
        }
        optional {
            padding: size
        }
    }
    
    theme test {
        // Missing required background property
        button {
            text: color(white)
        }
    }
    """
    with Path("test_theme.seed").open("w") as f:
        f.write(content)
        
    with pytest.raises(SeedParseError, match=r".*Missing required property: background.*"):
        parse_seed_file(Path("test_theme.seed"))
    
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
    """Test type validation rules"""
    content = """
    theme test {
        button {
            primary {
                // Invalid: color token doesn't exist
                background: color(nonexistent.500)
                
                // Invalid: size without unit
                padding: size(4)
                
                // Invalid: number as color
                text: color(42)
                
                // Invalid: string as number
                opacity: number("0.5")
            }
        }
    }
    """
    with Path("test_theme.seed").open("w") as f:
        f.write(content)
        
    with pytest.raises(SeedParseError, match=r".*Invalid type.*"):
        parse_seed_file(Path("test_theme.seed"))
    
    Path("test_theme.seed").unlink()
