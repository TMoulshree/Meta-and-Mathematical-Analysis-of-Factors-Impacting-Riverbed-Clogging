from pathlib import Path

def _find_root() -> Path:
    p = Path(__file__).resolve()
    for parent in [p] + list(p.parents):
        if (parent / ".git").exists() or (parent / "README.md").exists():
            return parent
    return Path.cwd().resolve()

ROOT = _find_root()
DATA = ROOT / "data"
RESULTS = ROOT / "results"
