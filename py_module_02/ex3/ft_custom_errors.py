class GardenError(Exception):
    def __init__(self, message: str = "A garden error occurred"):
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self, plant_name: str = "Banana",
                 message: str = "A plant error occurred"):
        super().__init__(message)
        self.plant_name = plant_name

    def __str__(self) -> str:
        return f"The {self.plant_name} plant is wilting~!"


class WaterError(GardenError):
    def __init__(self, message: str = "A water error occurred"):
        super().__init__(message)

    def __str__(self) -> str:
        return "Not enough water in the tank!"


def plant_error_test() -> None:
    print("Testing PlantError...")
    try:
        raise PlantError()
    except PlantError as e:
        print(f"Caught PlantError: {e}")


def water_error_test() -> None:
    print("Testing WaterError...")
    try:
        raise WaterError()
    except WaterError as e:
        print(f"Caught WaterError: {e}")


def garden_error_test() -> None:
    print("Testing catching all garden errors...")
    try:
        raise PlantError()
    except GardenError as e:
        print(f"Caught PlantError: {e}")

    try:
        raise WaterError()
    except GardenError as e:
        print(f"Caught WaterError: {e}")


if __name__ == "__main__":
    print("=== Custom Garden Errors Demo ===")
    print()
    plant_error_test()
    print()
    water_error_test()
    print()
    garden_error_test()
    print()
    print("All custom error types work correctly!")
