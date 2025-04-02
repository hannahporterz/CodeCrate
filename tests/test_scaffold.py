from pathlib import Path
from crate.scaffold import create_project


def test_create_project_tmp(tmp_path: Path):
    p = create_project(tmp_path, "xproj")
    assert (p / "README.md").exists()
    assert (p / "src").exists()

