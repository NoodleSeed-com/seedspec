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
        
    def generate(self, spec: dict, output_dir: str):
        """Generate React app from parsed spec"""
        os.makedirs(output_dir, exist_ok=True)
        os.makedirs(os.path.join(output_dir, 'src'), exist_ok=True)
        os.makedirs(os.path.join(output_dir, 'src/models'), exist_ok=True)
        os.makedirs(os.path.join(output_dir, 'src/screens'), exist_ok=True)
        
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
            
    def _generate_package_json(self, output_dir: str):
        """Generate package.json with required dependencies"""
        package = {
            "name": "seedspec-app",
            "version": "0.1.0",
            "private": True,
            "dependencies": {
                "react": "^17.0.2",
                "react-dom": "^17.0.2",
                "react-router-dom": "^5.2.0"
            },
            "scripts": {
                "start": "react-scripts start",
                "build": "react-scripts build"
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
