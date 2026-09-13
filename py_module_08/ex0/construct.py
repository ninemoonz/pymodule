import os
import sys
import site

# Detects whether it is running inside a virtual environment
# Displays information about the current Python environment
# Provides instructions for creating and activating a virtual environment if none is detected
# Show the diff between global and virtual environment package locations.


def in_venv() -> bool:
    return sys.prefix != sys.base_prefix


def matrix_stat(env: bool) -> str:
    if not env:
        message = "You're still plugged in"
    else:
        message = "Welcome to the construct"
    matrix_msg = f"MATRIX STATUS: {message}"
    return matrix_msg


def current_python(env: bool) -> str:
    if not env:
        return (f"Current Python: {sys.executable}\n"
                f"Virtual Environment: None detected")
    else:
        return (f"Current Python: {sys.executable}\n"
                f"Virtual Environment: {os.path.basename(sys.prefix)}\n"
                f"Environment Path: {sys.prefix}")


def package_site_path(env: bool) -> str:
    if not env:
        return ("To enter the construct, run:\n"
                "python -m matrix_env\n"
                "source matrix_env/bin/activate # On Unix\n"
                "matrix_env\\Scripts\\activate # On Windows\n"
                "\n"
                "Then run this program again.")
    else:
        return ("Package installation path:\n"
                f"{site.USER_SITE}")


def confirm_message(env: bool) -> str:
    if not env:
        return ("WARNING: You're in the global environment!\n"
                "The machines can see everything you install")
    else:
        return ("SUCCESS: You're in an isolated environments!\n"
                "Safe to install packages without affecting\n"
                "the global system.")


def message_struct(env: bool) -> None:
    print()
    print(matrix_stat(env))
    print()
    print(current_python(env))
    print()
    print(confirm_message(env))
    print()
    print(package_site_path(env))


if __name__ == "__main__":
    base_check = in_venv()
    message_struct(base_check)
