import sys
import typing


if __name__ == "__main__":
    arg_input = sys.argv
    if len(arg_input) == 1:
        print(f"Usage: {arg_input[0]} <file>")
    else:
        file_name: str = arg_input[1]
        f: typing.IO[str] | None = None
        print("=== Cyber Archive Recovery ===")
        print(f"Accessing file '{file_name}'")
        try:
            f = open(file_name, "r")
            print(f.read())
        except OSError as e:
            print(f"Error opening file '{file_name}': {e}")
        finally:
            if f:
                f.close()
                print(f"File '{file_name}' closed.")
