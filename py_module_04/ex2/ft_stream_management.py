#!/usr/bin/env python3

import sys
import typing


def print_archive(file_name: str) -> int:
    try:
        f: typing.IO[str] | None = None
        f = open(file_name, "r")
        print("---")
        print()
        print(f.read())
        print()
        print("---")
        return 1
    except OSError as e:
        sys.stderr.write(f"[STDERR] Error opening file '{sys.argv[1]}': {e}\n")
        return 0
    finally:
        if f:
            f.close()
            print(f"File '{file_name}' closed")


def transform_data(file_name: str) -> None:
    try:
        f: typing.IO[str] | None = None
        f = open(file_name, "r")
        fragment: str = f.read()
        split_str: list[str] = fragment.split("\n")
        transform_str: str = "#\n".join(split_str) + "#"
        print("Transform data:")
        print("---")
        print()
        print(transform_str)
        print()
        print("---")
        sys.stdout.write("Enter new file name (or emtpy): ")
        sys.stdout.flush()
        new_file: str = sys.stdin.readline().rstrip("\n")
        if len(new_file) == 0:
            print("Not saving data.")
        else:
            print(f"Saving data to '{new_file}'")
            n_f: typing.IO[str] = open(new_file, "w")
            n_f.write(transform_str)
            n_f.close()
            print(f"data saved in file '{new_file}'.")
    except OSError as e:
        sys.stderr.write(f"[STDERR] Error opening file '{sys.argv[1]}': {e}\n")
        print("Data not saved.")
    finally:
        if f:
            f.close()


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <file>")
    else:
        file_name: str = (sys.argv[1])
        print("=== Cyber Archives Recovery & Preservation ===")
        print(f"Accessing file '{file_name}'")
        if print_archive(file_name):
            print()
            transform_data(file_name)
