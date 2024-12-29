import os
import json
from jinja2 import Environment, FileSystemLoader

class Generator:
    def __init__(self, template_dir='templates'):
        self.env = Environment(
            loader=FileSystemLoader(os.path.join(os.path.dirname(__file__), template_dir))
        )
        
        # Add custom filters
        self.env.filters['lower'] = str.lower
        self.env.filters['input_type'] = self._input_type_for_field
        
        # Define valid types
        self.valid_types = {'text', 'num', 'bool'}
        
    def generate(self, spec: dict, output_dir: str):
        """Generate React app from parsed spec"""
        # Create directories
        os.makedirs(output_dir, exist_ok=True)
        os.makedirs(os.path.join(output_dir, 'src'), exist_ok=True)
        os.makedirs(os.path.join(output_dir, 'src/models'), exist_ok=True)
        os.makedirs(os.path.join(output_dir, 'src/screens'), exist_ok=True)
        os.makedirs(os.path.join(output_dir, 'public'), exist_ok=True)  # Add public directory
        
        # Generate public/index.html
        self._generate_index_html(output_dir)
        
        # Generate src/index.js
        self._generate_index_js(output_dir)
        
        # Generate App.js
        self._generate_file('App.js.tmpl', 
                          os.path.join(output_dir, 'src/App.js'),
                          spec)
        
        # Generate models
        for model in spec['models']:
            self._generate_file('Model.js.tmpl',
                              os.path.join(output_dir, f'src/models/{model["name"]}.js'),
                              model)
        
        # Generate screens
        for screen in spec['screens']:
            # Find corresponding model
            model = next(m for m in spec['models'] if m['name'] == screen['model'])
            screen['model'] = model
            
            self._generate_file('Screen.js.tmpl',
                              os.path.join(output_dir, f'src/screens/{screen["name"]}.js'),
                              screen)
                              
        # Generate package.json
        self._generate_package_json(output_dir)
        
    def _generate_file(self, template_name: str, output_path: str, context: dict):
        """Generate a single file from template"""
        # Add model references to context
        if isinstance(context, dict) and 'fields' in context:
            for field in context['fields']:
                if field['type'] not in self.valid_types:
                    field['is_reference'] = True
        template = self.env.get_template(template_name)
        with open(output_path, 'w') as f:
            f.write(template.render(**context))
            
    def _generate_index_html(self, output_dir: str):
        """Generate index.html"""
        html = '''
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title>SeedSpec App</title>
  </head>
  <body>
    <div id="root"></div>
  </body>
</html>
'''
        with open(os.path.join(output_dir, 'public/index.html'), 'w') as f:
            f.write(html.strip())

    def _generate_index_js(self, output_dir: str):
        """Generate index.js"""
        js = '''
import React from 'react';
import ReactDOM from 'react-dom';
import App from './App';

ReactDOM.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
  document.getElementById('root')
);
'''
        with open(os.path.join(output_dir, 'src/index.js'), 'w') as f:
            f.write(js.strip())

    def _generate_package_json(self, output_dir: str):
        """Generate package.json with minimal required dependencies"""
        package = {
            "name": "seedspec-app",
            "version": "0.1.0",
            "private": True,
            "dependencies": {
                "react": "^17.0.2",
                "react-dom": "^17.0.2",
                "react-router-dom": "^5.2.0",
                "react-scripts": "^5.0.1"
            },
            "scripts": {
                "start": "react-scripts start",
                "build": "react-scripts build"
            },
            "browserslist": {
                "production": [
                    ">0.2%",
                    "not dead",
                    "not op_mini all"
                ],
                "development": [
                    "last 1 chrome version"
                ]
            }
        }
        
        with open(os.path.join(output_dir, 'package.json'), 'w') as f:
            json.dump(package, f, indent=2)
            
    def _input_type_for_field(self, field_type: str) -> str:
        """Convert SeedSpec type to HTML input type"""
        types = {
            'text': 'text',
            'num': 'number',
            'bool': 'checkbox'
        }
        return types.get(field_type, 'text')
