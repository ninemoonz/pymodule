import sys
import typing


def print_archive(file_name: str) -> None:
    try:
        f: typing.IO[str] | None = None
        f = open(file_name, "r")
        fragment: str = f.read()
        print("---")
        print()
        print(fragment)
        print()
        print("---")
    except OSError as e:
        print(f"Error opening file '{sys.argv[1]}': {e}")
    finally:
        if f:
            f.close()
            print(f"File '{file_name}' closed")


def transform_data(file_name: str) -> None:
    try:
        f: typing.IO[str] | None = None
        f = open(file_name, "r")
        fragment: str = f.read()
        lines: list[str] = fragment.split("\n")
        new_content: str = "#\n".join(lines) + "#"
        print("Transform data:")
        print("---")
        print()
        print(new_content)
        print()
        print("---")
        new_file: str = input("Enter new file name (or emtpy): ")
        if len(new_file) == 0:
            print("Not saving data.")
        else:
            print(f"Saving data to '{new_file}'")
            n_f: typing.IO[str] = open(new_file, "w")
            n_f.write(new_content)
            n_f.close()
            print(f"data saved in file '{new_file}'.")
    except OSError as e:
        print(f"Error opening file '{sys.argv[1]}': {e}")


if __name__ == "__main__":
    if len(sys.argv) == 1:
        print(f"Usage: {sys.argv[0]} <file>")
    else:
        file_name: str = (sys.argv[1])
        print("=== Cyber Archives Recovery & Preservation ===")
        print(f"Accessing file '{file_name}'")
        print_archive(file_name)
        print()
        transform_data(file_name)
