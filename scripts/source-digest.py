from pathlib import Path
import hashlib

path = Path(__file__).resolve().parents[1] / "contracts" / "evidence_spend.py"
data = path.read_bytes()
print(f"path: {path.relative_to(path.parents[1])}")
print(f"bytes: {len(data)}")
print(f"sha256: {hashlib.sha256(data).hexdigest()}")
