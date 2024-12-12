import pytest
from pathlib import Path
from src.parser import parse_seed_file, SeedParseError

FIXTURES_DIR = Path(__file__).parent.parent / "fixtures" / "imports"

def test_basic_import():
    """Test basic import functionality"""
    result = parse_seed_file(FIXTURES_DIR / "main.seed")
    
    assert "Button" in result
    assert "light" in result
    assert result["light"]["colors"]["primary"] == "#ffffff"
    assert result["Button"]["styles"]["padding"] == "1rem"

def test_circular_import():
    """Test that circular imports are detected"""
    with pytest.raises(SeedParseError, match="Circular import detected"):
        parse_seed_file(FIXTURES_DIR / "circular1.seed")

def test_missing_import():
    """Test handling of missing import files"""
    with pytest.raises(SeedParseError, match="Import file not found"):
        parse_seed_file(FIXTURES_DIR / "missing.seed")

def test_relative_import():
    """Test relative path imports"""
    result = parse_seed_file(FIXTURES_DIR / "subdir/relative.seed")
    assert "Button" in result
    assert "Button" in result["SubApp"]["components"]

def test_multiple_imports():
    """Test multiple imports in same file"""
    result = parse_seed_file(FIXTURES_DIR / "multiple.seed")
    assert "light" in result
    assert "dark" in result
    assert "Button" in result
    assert "Card" in result
    assert len(result["MultiApp"]["themes"]) == 2
    assert len(result["MultiApp"]["components"]) == 2

def test_theme_import_values():
    """Test imported theme values are correct"""
    result = parse_seed_file(FIXTURES_DIR / "theme.seed")
    assert result["light"]["colors"]["primary"] == "#ffffff"
    assert result["light"]["colors"]["secondary"] == "#000000"
    assert result["dark"]["colors"]["primary"] == "#000000"
    assert result["dark"]["colors"]["secondary"] == "#ffffff"

def test_component_import_values():
    """Test imported component values are correct"""
    result = parse_seed_file(FIXTURES_DIR / "components.seed")
    assert result["Button"]["styles"]["padding"] == "1rem"
    assert result["Button"]["styles"]["background"] == "blue"
    assert result["Card"]["styles"]["margin"] == "1rem"
    assert result["Card"]["styles"]["shadow"] == "md"

def test_import_order():
    """Test that import order is preserved"""
    result = parse_seed_file(FIXTURES_DIR / "multiple.seed")
    keys = list(result.keys())
    assert keys.index("light") < keys.index("Button")
    assert keys.index("dark") < keys.index("Card")

def test_nested_imports():
    """Test that nested imports work correctly"""
    result = parse_seed_file(FIXTURES_DIR / "subdir/relative.seed")
    assert "Button" in result
    assert "SubApp" in result
    assert isinstance(result["SubApp"]["components"], list)
    assert "Button" in result["SubApp"]["components"]
