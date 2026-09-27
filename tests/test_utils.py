import subprocess
import sys


def test_main_exits_successfully():
    result = subprocess.run([sys.executable, "utils.py"], capture_output=True, text=True)
    assert result.returncode == 0


def test_main_output():
    result = subprocess.run([sys.executable, "utils.py"], capture_output=True, text=True)
    assert "Hello from utils.py" in result.stdout