import os
import sys
import site

# Detects whether it is running inside a virtual environment
# Displays information about the current Python environment
# Provides instructions for creating and activating a virtual environment if none is detected
# Show the diff between global and virtual environment package locations.


def in_venv() -> bool:
    return sys.prefix != sys.base_prefix


def matrix_stat(venv: bool) -> str:
    if not venv:
        message: str = "You're still plugged in"
    else:
        message = "welcome to the construct"
    return f"MATRIX STATUS: {message}"


if __name__ == "__main__":
    venv_check = in_venv()
    matrix_stat(venv_check)
