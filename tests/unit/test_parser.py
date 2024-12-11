import pytest
from pathlib import Path
from src.parser import parse_seed_file, SeedParseError

def test_parse_basic_theme():
    """Test parsing a basic theme definition"""
    content = """
    theme basic {
        colors {
            primary: "#000000"
        }
    }
    """
    with Path("test_theme.seed").open("w") as f:
        f.write(content)
        
    result = parse_seed_file(Path("test_theme.seed"))
    
    assert "basic" in result
    assert result["basic"]["colors"]["primary"] == "#000000"
    
    Path("test_theme.seed").unlink()

def test_parse_nested_structure():
    """Test parsing nested structures"""
    content = """
    theme test {
        typography {
            fontFamily {
                base: "Arial"
                heading: "Helvetica"
            }
        }
    }
    """
    with Path("test_theme.seed").open("w") as f:
        f.write(content)
        
    result = parse_seed_file(Path("test_theme.seed"))
    
    assert result["test"]["typography"]["fontFamily"]["base"] == "Arial"
    assert result["test"]["typography"]["fontFamily"]["heading"] == "Helvetica"
    
    Path("test_theme.seed").unlink()

def test_parse_value_types():
    """Test parsing different value types"""
    content = """
    theme types {
        values {
            string: "text"
            number: 42
            float: 3.14
            true_val: true
            false_val: false
        }
    }
    """
    with Path("test_theme.seed").open("w") as f:
        f.write(content)
        
    result = parse_seed_file(Path("test_theme.seed"))
    values = result["types"]["values"]
    
    assert values["string"] == "text"
    assert values["number"] == 42
    assert values["float"] == 3.14
    assert values["true_val"] is True
    assert values["false_val"] is False
    
    Path("test_theme.seed").unlink()

def test_parse_invalid_file():
    """Test handling of invalid files"""
    with pytest.raises(SeedParseError):
        parse_seed_file(Path("nonexistent.seed"))

def test_parse_invalid_syntax():
    """Test handling of invalid syntax"""
    content = """
    theme invalid {
        unclosed {
            key: value
        // Missing closing brace
    """
    with Path("test_theme.seed").open("w") as f:
        f.write(content)
        
    with pytest.raises(SeedParseError):
        parse_seed_file(Path("test_theme.seed"))
    
    Path("test_theme.seed").unlink()
