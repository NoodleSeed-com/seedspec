import pytest
import os
import tempfile
import json
from seed_compiler.generator import Generator

@pytest.fixture
def basic_spec():
    return {
        'app': {'name': 'Config', 'title': 'Config Testing'},
        'models': [{
            'name': 'Task',
            'fields': [
                {'name': 'title', 'type': 'text'}
            ]
        }],
        'screens': [{
            'name': 'Tasks',
            'model': 'Task'
        }]
    }

def test_tailwind_config(basic_spec):
    """Test Tailwind configuration generation"""
    with tempfile.TemporaryDirectory() as tmpdir:
        generator = Generator()
        generator.generate(basic_spec, tmpdir)
        
        config_path = os.path.join(tmpdir, 'tailwind.config.js')
        assert os.path.exists(config_path)
        
        with open(config_path) as f:
            content = f.read()
            
            # Check for required Tailwind configuration
            assert 'module.exports' in content
            assert 'content' in content
            assert './src/**/*.{js,jsx,ts,tsx}' in content
            assert 'theme' in content
            assert 'plugins' in content
            assert '@tailwindcss/forms' in content

def test_postcss_config(basic_spec):
    """Test PostCSS configuration generation"""
    with tempfile.TemporaryDirectory() as tmpdir:
        generator = Generator()
        generator.generate(basic_spec, tmpdir)
        
        config_path = os.path.join(tmpdir, 'postcss.config.js')
        assert os.path.exists(config_path)
        
        with open(config_path) as f:
            content = f.read()
            
            # Check for required PostCSS configuration
            assert 'module.exports' in content
            assert 'plugins' in content
            assert 'tailwindcss' in content
            assert 'autoprefixer' in content

def test_package_json(basic_spec):
    """Test package.json generation"""
    with tempfile.TemporaryDirectory() as tmpdir:
        generator = Generator()
        generator.generate(basic_spec, tmpdir)
        
        package_path = os.path.join(tmpdir, 'package.json')
        assert os.path.exists(package_path)
        
        with open(package_path) as f:
            package = json.load(f)
            
            # Check dependencies
            assert 'dependencies' in package
            assert 'react' in package['dependencies']
            assert 'react-dom' in package['dependencies']
            assert 'react-router-dom' in package['dependencies']
            assert '@tailwindcss/forms' in package['dependencies']
            assert 'tailwindcss' in package['dependencies']
            
            # Check scripts
            assert 'scripts' in package
            assert 'start' in package['scripts']
            assert 'build' in package['scripts']
            
            # Check browserslist
            assert 'browserslist' in package

def test_index_html(basic_spec):
    """Test index.html generation"""
    with tempfile.TemporaryDirectory() as tmpdir:
        generator = Generator()
        generator.generate(basic_spec, tmpdir)
        
        html_path = os.path.join(tmpdir, 'public/index.html')
        assert os.path.exists(html_path)
        
        with open(html_path) as f:
            content = f.read()
            
            # Check for required HTML elements
            assert '<!DOCTYPE html>' in content
            assert '<html lang="en">' in content
            assert '<div id="root">' in content
            assert '<meta charset="utf-8" />' in content
            assert '<meta name="viewport"' in content
            assert 'width=device-width' in content
            assert 'tailwindcss' in content

def test_index_css(basic_spec):
    """Test index.css generation"""
    with tempfile.TemporaryDirectory() as tmpdir:
        generator = Generator()
        generator.generate(basic_spec, tmpdir)
        
        css_path = os.path.join(tmpdir, 'src/index.css')
        assert os.path.exists(css_path)
        
        with open(css_path) as f:
            content = f.read()
            
            # Check for Tailwind directives
            assert '@tailwind base;' in content
            assert '@tailwind components;' in content
            assert '@tailwind utilities;' in content

def test_index_js(basic_spec):
    """Test index.js generation"""
    with tempfile.TemporaryDirectory() as tmpdir:
        generator = Generator()
        generator.generate(basic_spec, tmpdir)
        
        js_path = os.path.join(tmpdir, 'src/index.js')
        assert os.path.exists(js_path)
        
        with open(js_path) as f:
            content = f.read()
            
            # Check for React initialization
            assert 'import React' in content
            assert 'import ReactDOM' in content
            # Check for index.css import, independent of quote style
            assert any(variant in content for variant in ["import './index.css'", 'import "./index.css"'])
            assert 'import App from' in content
            assert 'ReactDOM.render(' in content
            assert '<React.StrictMode>' in content
            # Check for root element access, independent of quote style
            assert any(variant in content for variant in ["document.getElementById('root')", 'document.getElementById("root")'])
