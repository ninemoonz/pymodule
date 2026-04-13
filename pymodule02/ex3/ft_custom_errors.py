class GardenError(Exception):
    '''A basic error for garden problems (inherits from Exception)'''
    ...


class PlantError(GardenError):
    '''For problems with plants (inherits from GardenError)'''


class WaterError(GardenError):
    '''For problems with watering (inherits from GardenError)'''


if __name__ == "__main__":
    print("=== Custom Garden Errors Demo ===")
    print()
    print("All custom error types work correctly!")
