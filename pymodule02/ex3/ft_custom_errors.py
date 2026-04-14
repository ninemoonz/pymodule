class GardenError(Exception):
    '''A basic error for garden problems (inherits from Exception)'''
    def __init__(self, message: str = "A garden error occurred"):
        super().__init__(message)


class PlantError(GardenError):
    '''For problems with plants (inherits from GardenError)'''
    def __init__(self, message: str = "A plant error occurred"):
        super().__init__(message)


class WaterError(GardenError):
    '''For problems with watering (inherits from GardenError)'''
    def __init__(self, message: str = "A water error occurred"):
        super().__init__(message)


def plant_error_test():
    print("Testing PlantError...")
    try:
        raise PlantError("The tomato plant is wilting!")
    except PlantError as e:
        print(f"Caught PlantError: {e}")


def water_error_test():
    print("Testing WaterError...")
    try:
        raise WaterError("Not enough water in the tank!")
    except WaterError as e:
        print(f"Caught WaterError: {e}")


def garden_error_test():
    print("Testing catching all garden errors...")
    try:
        raise PlantError("The tomato plant is wilting!")
    except GardenError as e:
        print(f"Caught PlantError: {e}")

    try:
        raise WaterError("Not enough water in the tank!")
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
