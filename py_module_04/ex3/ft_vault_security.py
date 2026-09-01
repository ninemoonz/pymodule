#!/usr/bin/env python3


def secure_archive(file_name: str, action: str,
                   file_content: str = "") -> tuple[bool, str]:
    result_flag: bool = False
    try:
        with open(file_name, action) as file:
            if action == "r":
                result_flag = True
            elif action == "w":
                result_flag = True
                new_file = open(file_name, action)
                new_file.write(file_content)
                return (result_flag, "Content successfully written to file")
            return (result_flag, file.read())
    except OSError as e:
        return (result_flag, str(e))


if __name__ == "__main__":
    print("=== Cyber Archive Security ===")
    print()
    print("Using 'secure_archive' to read from a nonexistent file:")
    example1 = secure_archive("foo", "r", "y")
    print(example1)
    print()
    print("Using 'secure_archive' to read from an inaccessible file:")
    example2 = secure_archive("master.passwd", "r", "y")
    print(example2)
    print()
    print("Using 'secure_archive' to read from a regular file:")
    example3 = secure_archive("ancient_fragment.txt", "r", "n")
    print(example3)
    print()
    print("Using 'secure_archive' to write previous content to a new file:")
    example4 = secure_archive("new_fragment.txt", "w", example3[1])
    print(example4)
