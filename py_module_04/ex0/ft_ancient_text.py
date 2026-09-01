import sys
import typing


def print_archive(file_name: str) -> None:
    try:
        f: typing.IO[str] | None = None
        f = open(file_name, "r")
        print("---")
        print()
        print(f.read())
        print()
        print("---")
    except OSError as e:
        print(f"Error opening file '{sys.argv[1]}': {e}")
    finally:
        if f:
            f.close()
            print(f"File '{file_name}' closed")


if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("Usage: ft_ancient_text.py <file>")
    else:
        file_name: str = (sys.argv[1])
        print("=== Cyber Archives Recovery ===")
        print(f"Accessing file '{file_name}'")
        print_archive(file_name)
