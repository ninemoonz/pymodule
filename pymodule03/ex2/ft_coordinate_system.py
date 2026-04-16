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


def first_formula(tuple_list: tuple):
    x_1 = tuple_list[0]
    y_1 = tuple_list[1]
    z_1 = tuple_list[2]

    distance = math.sqrt((0 - x_1)**2 + (0 - y_1)**2 + (0 - z_1)**2)
    return distance


'''
def second_formula(tuple_one: tuple, tuple_two: tuple):
    x_1 = tuple_one[0]
    y_1 = tuple_one[1]
    z_1 = tuple_one[2]

    x_2 = tuple_two[0]
    y_2 = tuple_two[1]
    z_2 = tuple_two[2]
'''


if __name__ == "__main__":
    print("=== Game Coordinate System ===")
    print()
    result = get_player_pos()
    tuple_result = tuple(result)
    print(f"{first_formula(tuple_result):.4f}")
    print()
