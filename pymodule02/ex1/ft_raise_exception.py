def input_temperature(temp_str: str) -> int:
    temp_int = int(temp_str)
    if temp_int < 0:
        raise ValueError(f"{temp_int}°C is too cold for plants (min 0°C)")
    elif temp_int > 40:
        raise ValueError(f"{temp_int}°C is too hot for plants (max 40°C)")
    else:
        return temp_int


def test_temperature(temp_str: str) -> None:
    print(f"Input data is '{temp_str}'")
    result: int = 0
    try:
        result = input_temperature(temp_str)
    except Exception as e:
        print(f"Caught input_temperature error: {e}")
    else:
        print(f"Temperature is now {result}°C")


if __name__ == "__main__":
    print("=== Garden Temperature ===")
    print()
    test_temperature("23")
    print()
    test_temperature("23abc")
    print()
    test_temperature("100")
    print()
    test_temperature("-50")
    print()
    print("All tests completed - program didn't crash!")
