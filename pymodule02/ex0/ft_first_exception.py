def input_temperature(temp_str: str) -> int:
    temp_int = int(temp_str)
    return temp_int


def test_temperature(temp_str: str) -> None:
    print(f"Input data is '{temp_str}'")
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
    print("All tests completed - program didn't crash!")
