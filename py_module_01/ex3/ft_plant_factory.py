class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

    def grow(self) -> None:
        if self.name == "Potato":
            self.height += 3
        elif self.name == "Tomato":
            self.height += 2
        elif self.name == "Bamboo":
            self.height += 15
        else:
            self.height += 1

    def get_info(self) -> None:
        print(
            f"Created: {self.name}: "
            f"{self.height}cm, {self.age} days old"
            )


def ft_plant_factory(name: str, height: int, age: int) -> Plant:
    plant = Plant(name, height, age)
    print(f"Created: {plant.name}: {plant.height:.1f}cm, {plant.age} days old")
    return plant


if __name__ == "__main__":
    print("=== Plant Factory Output ===")
    rose = ft_plant_factory("Rose", 25, 42)
    oak = ft_plant_factory("Oak", 300, 421)
    cactus = ft_plant_factory("Cactus", 10, 89)
    sunflower = ft_plant_factory("SunFlower", 132, 24)
    fern = ft_plant_factory("Fern", 10, 17)
