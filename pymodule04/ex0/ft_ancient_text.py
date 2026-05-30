import sys
import typing


if __name__ == "__main__":
    arg_input = sys.argv
    if len(arg_input) == 1:
        print(f"Usage: {arg_input[0]} <file>")
