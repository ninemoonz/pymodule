import math


class InputError(Exception):
    pass


def input_request(coordinate: str) -> int:
    while True:
        try:
            x = int(input(f"player position {coordinate}: "))
            break
        except Exception as e:
            print(f"Not a proper input: {e}")
    return x


def get_player_pos() -> None:
    x = input_request("x")
    y = input_request("y")
    z = input_request("z")
    coordinate: tuple = (x, y, z)
    print(coordinate)


if __name__ == "__main__":
    print("=== Game Coordinate System ===")
    get_player_pos()
