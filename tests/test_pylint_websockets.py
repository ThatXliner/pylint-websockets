import subprocess
from pathlib import Path


def test_main():
    process = subprocess.run(
        ["pylint", "--load-plugins=pylint_websockets", "some_file.py"],
        capture_output=True,
        check=False,
        cwd=Path(__file__).parent,
    )
    assert process.returncode == 0, (process.stdout, process.stderr)
