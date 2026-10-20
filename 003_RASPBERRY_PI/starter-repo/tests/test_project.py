from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def test_readme_exists():
    assert (ROOT / "README.md").exists()


def test_expected_folders_exist():
    for name in ("arduino", "pi", "tests", "docs"):
        assert (ROOT / name).is_dir(), f"missing folder: {name}/"
