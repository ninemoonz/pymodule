import math


class InputError(Exception):
    pass


class SyntaxError(InputError):
    pass


class ConvertError(InputError):
    pass


def split_test(str_pos: str) -> list:
    split_input = str_pos.split(",")
    if len(split_input) < 3:
        raise SyntaxError("Invalid syntax")
    return split_input


def convert_test(str_element: str) -> float:
    try:
        return float(str_element)
    except ValueError:
        raise ConvertError(f"Error on parameter '{str_element}': "
                           "could not convert string to float:  "
                           f"'{str_element}'")


def get_player_pos():
    while True:
        input_pos = input("Enter new coordinates as "
                          "floats in format 'x,y,z': ")
        float_list: list = []
        try:
            split_list = split_test(input_pos)
            for element in split_list:
                int_element = convert_test(element)
                float_list.append(int_element)
            return float_list
        except InputError as e:
            print(e)


def distance_formula(int_list: list):
    ...


if __name__ == "__main__":
    print("=== Game Coordinate System ===")
    print()
    result = get_player_pos()
    print(result)
    print()
