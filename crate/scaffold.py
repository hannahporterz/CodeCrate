import argparse
from pathlib import Path
from typing import Dict


DEFAULT_FILES: Dict[str, str] = {
    "README.md": "# New Project\n\nShort description.\n",
    "LICENSE": "MIT License (placeholder)\n",
    ".gitignore": ".DS_Store\nnode_modules\nvenv/\n*.log\n",
}


def create_project(root: Path, name: str):
    project_dir = root / name
    project_dir.mkdir(parents=True, exist_ok=True)
    for rel, content in DEFAULT_FILES.items():
        p = project_dir / rel
        if not p.exists():
            p.write_text(content)
    (project_dir / "src").mkdir(exist_ok=True)
    return project_dir


def main(argv=None):
    parser = argparse.ArgumentParser(description="Scaffold a simple project")
    parser.add_argument("name", help="Project name")
    parser.add_argument("--into", default=".", help="Target directory")
    args = parser.parse_args(argv)
    root = Path(args.into).resolve()
    created = create_project(root, args.name)
    print(str(created))


if __name__ == "__main__":
    main()
