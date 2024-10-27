import os
from pathlib import Path
from anthropic import Anthropic

SYSTEM_PROMPT = """You are an expert full-stack application generator that creates production-ready code from SeedML specifications.

Follow these strict guidelines:
1. Use only these technologies:
   - Frontend: React 18 + TypeScript + Tailwind CSS + React Query + React Router + React Hook Form
   - Backend: FastAPI + SQLAlchemy + Pydantic + Alembic
   - Database: MySQL 8
   - Testing: Jest (frontend), pytest (backend)
   - Documentation: OpenAPI/Swagger

2. Code structure:
   - Frontend: Feature-based architecture with shared components
   - Backend: Clean architecture with services, repositories, and DTOs
   - Database: Follow strict naming conventions (snake_case, plural tables)

3. Patterns:
   - Use React Query for all API calls
   - Implement proper error boundaries
   - Follow repository pattern for database access
   - Use dependency injection
   - Implement proper validation at all layers

4. Security:
   - JWT authentication
   - Role-based access control
   - Input validation
   - SQL injection prevention
   - XSS protection

5. Docker Compose:
   - Include services for frontend, backend, and database
   - Set up environment variables
   - Provide volume mounts for database

6. Kubernetes:
   - Generate Deployment, Service, and Ingress manifests
   - Use environment variables for configuration
   - Provide persistent volume claim for database
   - Include Helm chart for easy deployment"""

class SeedMLGenerator:
    def __init__(self, api_key):
        self.client = Anthropic(api_key=api_key)
        
    def generate_application(self, seed_file):
        seed_content = Path(seed_file).read_text()
        app_name = Path(seed_file).stem
        
        # Create output directory
        os.makedirs(app_name, exist_ok=True)
        
        # Generate complete application
        response = self.generate_code(seed_content)
        self.write_files(app_name, response)
        
    def generate_code(self, seed_content):
        prompt = f"""Generate a complete, production-ready application from this SeedML specification:

{seed_content}

Follow these additional requirements:

1. Frontend Structure:
```
frontend/
  ├── src/
  │   ├── components/
  │   │   ├── common/
  │   │   └── features/
  │   ├── hooks/
  │   ├── services/
  │   ├── types/
  │   ├── utils/
  │   └── App.tsx
  └── package.json
```

2. Backend Structure:
```
backend/
  ├── app/
  │   ├── api/
  │   ├── core/
  │   ├── services/
  │   └── repositories/
  ├── tests/
  └── main.py
```

3. Database:
- Use meaningful table names
- Include proper indexes
- Set up foreign key constraints
- Include initial migrations

4. Features:
- Complete CRUD operations
- Error handling
- Loading states
- Form validation
- API documentation
- Authentication/Authorization
- Database migrations
- Logging
- Testing

Generate ALL necessary files with complete, production-ready code."""

        response = self.client.messages.create(
            model="claude-3-sonnet-20240229",
            max_tokens=150000,
            temperature=0,
            system=SYSTEM_PROMPT,
            messages=[{"role": "user", "content": prompt}]
        )
        
        return response.content

    def write_files(self, app_name, response):
        # Parse file list
        file_list_start = response.find("<file_list>") + len("<file_list>")
        file_list_end = response.find("</file_list>")
        file_list = response[file_list_start:file_list_end].strip().split("\n")

        # Write each file
        for filename in file_list:
            file_start = response.find(f"<file:{filename}>") + len(f"<file:{filename}>")
            file_end = response.find("</file>", file_start)
            
            if file_start > 0 and file_end > 0:
                content = response[file_start:file_end].strip()
                
                # Create full path
                full_path = os.path.join(app_name, filename)
                os.makedirs(os.path.dirname(full_path), exist_ok=True)
                
                # Write file
                with open(full_path, 'w') as f:
                    f.write(content)
                print(f"Generated: {filename}")
