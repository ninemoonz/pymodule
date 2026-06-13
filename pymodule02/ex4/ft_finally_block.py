class PlantError(Exception):
    '''For problems with plants (inherits from GardenError)'''
    def __init__(self, message: str):
        self.message = message
        super().__init__(message)


def water_plant(plant_name: str):
    if not plant_name == plant_name.capitalize():
        raise PlantError(f"Invalid plant name to water: {plant_name}")
    print(f"Watering {plant_name}: [OK]")


def watering_system(plant_list: list):
    print("Opening Watering System")
    try:
        for plant in plant_list:
            water_plant(plant)
    except PlantError as e:
        print(f"Caught Plant Error: {e}")
    finally:
        print("...ending test and return to main")
        print("Closing water system")


if __name__ == "__main__":
    valid_list = ["Tomato", "Lettuce", "Rose"]
    invalid_list = ["Tomato", "lettuce", "Rose"]

    print("Testing valid plants...") 
    watering_system(valid_list)
    print()
    print("Testing invalid plants...")
    watering_system(invalid_list)
    

