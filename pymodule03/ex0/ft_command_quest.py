import sys

if __name__ == "__main__":
    sys_list = sys.argv
    print("=== Command Quest ===")
    print(f"Program name: {sys_list[0]}")
    if len(sys_list) == 1:
        print("No arguments provided")
    elif len(sys_list) > 1:
        print(f"Arguments received: {len(sys_list) - 1}")
        for i in range(1, len(sys_list)):
            print(f"Argument {i}: {sys_list[i]}")
    print(f"Total arguments: {len(sys_list)}")
    print()
