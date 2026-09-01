#!/usr/bin/python3

class Plant:
    def __init__(self, name: str):
        self.name = name


class GardenError(Exception):
    def __init__(self, message: str = "A garden error occurred"):
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self, name: str, message: str = "A plant error occurred"):
        super().__init__(message)
        self.name = name

    def __str__(self) -> str:
        return f"Invalid plant name to water: '{self.name}'"


class WaterError(GardenError):
    def __init__(self, message: str = "A water error occurred"):
        super().__init__(message)


def water_plant(plant: Plant) -> None:
    if plant.name != plant.name.capitalize():
        raise PlantError(plant.name)
    else:
        print(f"Watering {plant.name}: [OK]")


def test_watering_system(plant_list: list[Plant]) -> None:
    print("Testing valid plants...")
    print("Opening watering system")
    try:
        for plant in plant_list:
            water_plant(plant)
    except PlantError as e:
        print(f"Caught PlantError: {e}")
        print(".. ending tests and returing to main")
        return
    finally:
        print("Closing watering system")


if __name__ == "__main__":
    plant_list = [Plant("Rose"), Plant("Cactus"), Plant("Fern")]
    plant_list2 = [Plant("Rose"), Plant("cactus"), Plant("Fern")]

    print("=== Garden Watering System ===")
    print()
    test_watering_system(plant_list)
    print()
    test_watering_system(plant_list2)
    print()
    print("Cleanup always happens, even with errors")
