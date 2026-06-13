import sys


def str_parse(arg_list: list[str]) -> None:
    parse_list: list[str] = []
    for arg_element in arg_list:
        parse_list = arg_element.split(":")
        print(parse_list)
        parse_dict = {parse_list[0]: parse_list[1]}
        print(parse_dict)


if __name__ == "__main__":
    arg_list: list[str] = []
    if len(sys.argv) <= 1:
        print("Not enough arguments")
    else:
        for i in range(1, len(sys.argv)):
            arg_list.append(sys.argv[i])
    str_parse(arg_list)
