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

def test_multiple_imports():
    """Test multiple imports in same file"""
    result = parse_seed_file(FIXTURES_DIR / "multiple.seed")
    assert "light" in result
    assert "dark" in result
    assert "Button" in result
