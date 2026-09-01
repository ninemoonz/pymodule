class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

    def show(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.age} days old")


class Flower(Plant):
    def __init__(self, name: str, height: float, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self.color = color
        self.bloom = False

    def show(self) -> None:
        super().show()
        print(f"Color: {self.color}")
        if self.bloom:
            print(f"{self.name} is blooming beautifully!")
        else:
            print(f"{self.name} has not bloomed yet")

    def bloom_flower(self) -> None:
        self.bloom = True
        print(f"[asking {self.name} to bloom]")


class Tree(Plant):
    def __init__(self, name: str, height: float,
                 age: int, trunk_diameter: float) -> None:
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def show(self) -> None:
        super().show()
        print(f"Trunk diameter: {self.trunk_diameter}cm")

    def produce_shade(self) -> None:
        print(f"[asking the {self.name} to produce shade]")
        print(f"Tree {self.name} provides a shade of "
              f"{self.height}cm long and {self.trunk_diameter}cm wide")


class Vegetable(Plant):
    def __init__(self, name: str, height: float, age: int,
                 harvest_season: str, nutritional_value: int) -> None:
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def show(self) -> None:
        super().show()
        print(f"Harvest season: {self.harvest_season}")
        print(f"Nutrition value: {self.nutritional_value}")

    def vegetable_nut(self, days: int) -> None:
        print(f"[make {self.name} grow and age for {days} days]")
        self.age += days
        self.nutritional_value += days


if __name__ == "__main__":
    rose = Flower("Rose", 25, 30, "red")
    oak = Tree("Oak", 500.0, 1852, 50.0)
    carrot = Vegetable("Carrot", 15.0, 43, "November", 0)
    print("=== Garden Plant Types ===")
    print("=== Flower")
    rose.show()
    rose.bloom_flower()
    rose.show()
    print()
    print("=== Tree")
    oak.show()
    oak.produce_shade()
    print()
    print("=== Vegetable")
    carrot.show()
    carrot.vegetable_nut(20)
    carrot.show()
