import os
import json
from pathlib import Path

# Root project name
ROOT = Path("smart-barangay-system")

# Directory structure
STRUCTURE = {
    "apps": {
        "backend": {
            "src": {
                "modules": {
                    "auth": {
                        "auth.controller.ts": "",
                        "auth.service.ts": "",
                        "auth.module.ts": ""
                    },
                    "residents": {
                        "residents.controller.ts": "",
                        "residents.service.ts": "",
                        "residents.module.ts": ""
                    },
                    "gis": {
                        "gis.controller.ts": "",
                        "gis.service.ts": "",
                        "gis.module.ts": ""
                    }
                },
                "main.ts": "import { NestFactory } from '@nestjs/core';\nimport { AppModule } from './app.module';\n\nasync function bootstrap() {\n  const app = await NestFactory.create(AppModule);\n  await app.listen(3001);\n  console.log('Backend running on http://localhost:3001');\n}\nbootstrap();\n",
                "app.module.ts": "import { Module } from '@nestjs/common';\nimport { AuthModule } from './modules/auth/auth.module';\nimport { ResidentsModule } from './modules/residents/residents.module';\nimport { GisModule } from './modules/gis/gis.module';\n\n@Module({ imports: [AuthModule, ResidentsModule, GisModule] })\nexport class AppModule {}\n"
            },
            "package.json": json.dumps({
                "name": "backend",
                "version": "1.0.0",
                "scripts": {
                    "start": "nest start",
                    "start:dev": "nest start --watch"
                },
                "dependencies": {
                    "@nestjs/common": "^10.0.0",
                    "@nestjs/core": "^10.0.0",
                    "@nestjs/platform-express": "^10.0.0",
                    "reflect-metadata": "^0.2.0",
                    "rxjs": "^7.8.0",
                    "pg": "^8.10.0",
                    "@supabase/supabase-js": "^2.42.0"
                },
                "devDependencies": {
                    "typescript": "^5.3.0",
                    "@nestjs/cli": "^10.0.0",
                    "@types/node": "^20.0.0"
                }
            }, indent=2)
        },
        "frontend": {
            "src": {
                "app": {
                    "page.tsx": "export default function Home() { return <h1>Welcome to Smart Barangay System</h1>; }",
                    "layout.tsx": "export default function Layout({ children }) { return <html><body>{children}</body></html>; }"
                }
            },
            "package.json": json.dumps({
                "name": "frontend",
                "version": "1.0.0",
                "scripts": {
                    "dev": "next dev",
                    "build": "next build",
                    "start": "next start"
                },
                "dependencies": {
                    "next": "15.0.0",
                    "react": "19.0.0",
                    "react-dom": "19.0.0",
                    "tailwindcss": "^3.4.0",
                    "@supabase/supabase-js": "^2.42.0"
                },
                "devDependencies": {
                    "typescript": "^5.3.0",
                    "autoprefixer": "^10.4.0",
                    "postcss": "^8.4.0"
                }
            }, indent=2),
            "tailwind.config.js": "module.exports = { content: ['./src/**/*.{js,ts,jsx,tsx}'], theme: { extend: {} }, plugins: [] }",
            "tsconfig.json": json.dumps({
                "compilerOptions": {
                    "jsx": "preserve",
                    "strict": True,
                    "module": "ESNext",
                    "target": "ES6",
                    "baseUrl": "./src"
                }
            }, indent=2)
        }
    },
    "packages": {
        "shared-types": {"index.ts": "export interface Resident { id: number; name: string; address: string; }"},
        "utils": {"index.ts": "export function formatName(name: string) { return name.toUpperCase(); }"}
    },
    "supabase": {
        "migrations": {"001_init.sql": "-- Example SQL migration\nCREATE TABLE residents (id SERIAL PRIMARY KEY, name TEXT, address TEXT);"},
        "functions": {"on_new_resident.ts": "// Example Supabase Edge Function\nexport const handler = async (event) => { console.log('New resident added'); };"}
    },
    "docs": {
        "README.md": "# Smart Barangay Management System\nGenerated project structure.\n"
    }
}

# Base configuration files
BASE_FILES = {
    "package.json": json.dumps({
        "name": "smart-barangay-system",
        "private": True,
        "workspaces": ["apps/*", "packages/*"],
        "scripts": {
            "dev": "turbo run dev --parallel"
        },
        "devDependencies": {
            "turbo": "^2.0.0"
        }
    }, indent=2),
    "tsconfig.base.json": json.dumps({
        "compilerOptions": {
            "strict": True,
            "moduleResolution": "node",
            "esModuleInterop": True,
            "skipLibCheck": True
        }
    }, indent=2),
    "turbo.json": json.dumps({
        "$schema": "https://turbo.build/schema.json",
        "pipeline": {
            "dev": {"cache": False}
        }
    }, indent=2),
    ".env.example": "SUPABASE_URL=\nSUPABASE_ANON_KEY=\n",
    "README.md": "# Smart Barangay Management System\n\nMonorepo powered by NestJS + Next.js + Supabase."
}


def create_structure(base_path, structure):
    """Recursively create folders and files."""
    for name, content in structure.items():
        path = base_path / name
        if isinstance(content, dict):
            path.mkdir(parents=True, exist_ok=True)
            create_structure(path, content)
        else:
            with open(path, "w", encoding="utf-8") as f:
                f.write(content)


def main():
    print("🚀 Creating Smart Barangay System structure...")
    ROOT.mkdir(exist_ok=True)

    # Create directory structure
    create_structure(ROOT, STRUCTURE)

    # Create root config files
    for name, content in BASE_FILES.items():
        (ROOT / name).write_text(content, encoding="utf-8")

    print("\n✅ Structure created successfully at:", ROOT.resolve())
    print("\nNext steps:")
    print("1. cd smart-barangay-system")
    print("2. npm install --workspaces")
    print("3. cd apps/backend && npm run start:dev  # start API")
    print("4. cd ../frontend && npm run dev         # start web app")


if __name__ == "__main__":
    main()
