#!/usr/bin/python3

import sys


class ParsingError(Exception):
    pass


class QuantityError(Exception):
    pass


class RedundantError(Exception):
    pass


def parsing_test(input_str: str) -> tuple[str, str]:
    if ':' not in input_str:
        raise ParsingError(f"invalid parameter '{input_str}'")
    else:
        key, value = input_str.split(':')
    return key, value


def quantity_test(key: str, value: str) -> dict[str, int]:
    invent_dict: dict[str, int] = {}
    try:
        invent_dict[key] = int(value)
        if int(value) < 0:
            raise QuantityError(f"Quantity cannot be negative: {value}")
        return invent_dict
    except ValueError as e:
        raise QuantityError(e)


def redundant_test(dict_list: dict[str, int],
                   new_dict: dict[str, int]) -> None:
    for key in new_dict:
        if key in dict_list:
            raise RedundantError(f"Redundant item '{key}' - discarding")


def inventory_input(input_list: list[str]) -> dict[str, int]:
    invent_dict: dict[str, int] = {}
    for input_str in input_list:
        try:
            key, value = parsing_test(input_str)
        except ParsingError as e:
            print(f"Error - {e}")
            continue
        try:
            new_dict = quantity_test(key, value)
        except QuantityError as e:
            print(f"Quantity error for '{key}': {e}")
            continue
        try:
            redundant_test(invent_dict, new_dict)
        except RedundantError as e:
            print(e)
            continue
        invent_dict.update(new_dict)
    return invent_dict


def max_finder(invent_dict: dict[str, int]) -> None:
    max_val: int = 0
    max_key: str = ""
    for key in invent_dict:
        if invent_dict[key] > max_val:
            max_val = invent_dict[key]
            max_key = key
    print(f"Item most abundant: {max_key} with quantity {max_val}")


def min_finder(invent_dict: dict[str, int]) -> None:
    min_key: str = list(invent_dict.keys())[0]
    min_val: int = invent_dict[min_key]
    for key in invent_dict:
        if invent_dict[key] < min_val:
            min_val = invent_dict[key]
            min_key = key
    print(f"Item least abundant: {min_key} with quantity {min_val}")


def inventory_analysis(invent_dict: dict[str, int]) -> None:
    if not invent_dict:
        print("Inventory is empty, nothing to analyze")
        return
    total_item = sum(invent_dict.values())
    print(f"Got inventory: {invent_dict}")
    print(f"Item list: {list(invent_dict.keys())}")
    print(f"Total quantity of the {len(invent_dict.keys())} items: "
          f"{total_item}")
    for key in invent_dict:
        print(f"Item {key} represents "
              f"{round((invent_dict[key] / total_item) * 100, 1)}%")
    max_finder(invent_dict)
    min_finder(invent_dict)
    invent_dict.update({"magic_item": 1})
    print(f"Updated inventory: {invent_dict}")


if __name__ == "__main__":
    print("=== Inventory System Analysis ===")
    input_arg = sys.argv
    if len(input_arg) <= 1:
        print("Not arguments passed in. Insert <item_name>:<quantity>")
    else:
        dict_result: dict[str, int] = inventory_input(input_arg[1:])
    inventory_analysis(dict_result)
