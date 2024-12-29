import pytest
import os
import tempfile
from pathlib import Path
from seed_compiler.cli import main

def test_cli_missing_input(capsys):
    """Test CLI with missing input file"""
    with pytest.raises(SystemExit) as e:
        main(['nonexistent.seed'])
    
    assert e.value.code == 1
    captured = capsys.readouterr()
    assert "Error: Input file not found" in captured.err

def test_cli_basic_generation(capsys, tmp_path):
    """Test basic CLI generation"""
    # Create test input file
    input_file = tmp_path / "test.seed"
    input_file.write_text("""
    model Task {
        title text
        done bool = false
    }
    
    screen Tasks using Task
    """)
    
    # Create output dir
    output_dir = tmp_path / "output"
    
    # Run CLI
    with pytest.raises(SystemExit) as e:
        main([str(input_file), '-o', str(output_dir)])
    
    assert e.value.code == 0
    
    # Check output
    assert os.path.exists(output_dir)
    assert os.path.exists(output_dir / 'src')
    assert os.path.exists(output_dir / 'package.json')

def test_cli_verbose_output(capsys, tmp_path):
    """Test verbose output mode"""
    # Create test input
    input_file = tmp_path / "test.seed"
    input_file.write_text("""
    model Task {
        title text
    }
    screen Tasks using Task
    """)
    
    # Run CLI with verbose flag
    with pytest.raises(SystemExit) as e:
        main([str(input_file), '-v'])
    
    captured = capsys.readouterr()
    assert "Reading input file" in captured.out
    assert "Parsing SeedSpec file" in captured.out
    assert "Successfully generated" in captured.out
