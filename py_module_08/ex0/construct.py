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
        message = "You're still plugged in"
    else:
        message = "Welcome to the construct"
    matrix_msg = f"MATRIX STATUS: {message}"
    return matrix_msg


def current_path() -> str:
    return sys.prefix


def package_site_path(venv: bool) -> str:
    if not venv:
        return ("To enter the construct, run:\n"
                "python -m matrix_env\n"
                "source matrix_env/bin/activate # On Unix\n"
                "matrix_env\\Scripts\\activate # On Windows\n"
                "\n"
                "Then run this program again.")
    else:
        return ("Package installation path:\n"
                f"{site.USER_SITE}")


def confirm_message(venv: bool) -> str:
    if not venv:
        return ("WARNING: You're in the global environment!\n"
                "The machines can see everything you install")
    else:
        return ("SUCCESS: You're in an isolated environments!\n"
                "Safe to install packages without affecting\n"
                "the global system.")


if __name__ == "__main__":
    print()
    print(matrix_stat(in_venv()))
    print()
    print(f"Current Python: {current_path()}")
    print()
    print(f"{confirm_message(in_venv())}")
    print()
    print(package_site_path(in_venv()))
