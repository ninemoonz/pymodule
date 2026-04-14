class Plant:
    def __init__(self, name: str):
        self.name = name


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


def water_plant(plant_name: str):
    if not plant_name == plant_name.capitalize():
        raise PlantError(f"Invalid plant name to water: {plant_name}")


if __name__ == "__main__":
    ...