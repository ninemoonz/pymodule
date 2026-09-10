import os
import sys
import site


def in_venv():
    return sys.prefix != sys.base_prefix


def matrix_stat(venv: bool):
    if not venv:
        print("MATRIX STATUS: You're still plugged in")
        print()
        print(f"Current Python: {sys.prefix}")
        print("Virtual Environment: None Detected")
        print()
        print("WARNING: You're in the global environment!")
        print("The machines can see everything you install.")
        print()
        print("To enter the construct, run:")
        print("python -m venv matrix_env")
        print("source matrix_env/bin/activate # On Unix")
        print("matrix_env\\Script\\activate # On Windows")
        print()
        print("Then run this program again")
    else:
        


if __name__ == "__main__":
    venv_check = in_venv()
    matrix_stat(venv_check)
