from pathlib import Path

# Project root
project_root = Path.cwd()

# List of folders to create
folders = [
    "data/raw",
    "data/processed",
    "notebooks",
    "src/data",
    "src/features",
    "src/models",
    "src/utils",
    "models",
    "reports/figures",
    "reports/profiling",
    "app",
    "mlruns"
]

# Create folders
for folder in folders:
    (project_root / folder).mkdir(parents=True, exist_ok=True)

print("Project folder structure created successfully!")