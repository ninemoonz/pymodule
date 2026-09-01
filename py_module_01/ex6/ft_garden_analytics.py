class Plant:
    class _Stats:
        def __init__(self) -> None:
            self._grow_count = 0
            self._age_count = 0
            self._show_count = 0
            self._shade_count = 0

        def increment_grow(self) -> None:
            self._grow_count += 1

        def increment_age(self) -> None:
            self._age_count += 1

        def increment_show(self) -> None:
            self._show_count += 1

        def increment_shade(self) -> None:
            self._shade_count += 1

        def stat_display(self) -> None:
            print(f"Stats: {self._grow_count} grow, "
                  f"{self._age_count} age, "
                  f"{self._show_count} show")

    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age
        self._stats = self._Stats()

    def show(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.age} days old")
        self._stats.increment_show()

    @staticmethod
    def check_year(age: int) -> None:
        check = False
        if age > 365:
            check = True
        else:
            check = False
        print(f"Is {age} days more than a year? -> ", check)

    @classmethod
    def anonymous_plant(cls) -> "Plant":
        unknown_plant = Plant("Unknown plant", 0.0, 0)
        return unknown_plant


class Flower(Plant):
    def __init__(self, name: str, height: float, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self.color = color
        self.bloom = False

    def bloom_flower(self) -> None:
        print(f"[asking the {self.name} to grow and bloom]")
        self.bloom = True
        self.height += 10
        self._stats.increment_grow()

    def show(self) -> None:
        super().show()
        print(f"Color: {self.color}")
        if self.bloom:
            print(f"{self.name} is blooming beautifully!")
        else:
            print(f"{self.name} has not bloomed yet")


class Tree(Plant):
    class _Stats(Plant._Stats):
        def stat_display(self) -> None:
            super().stat_display()
            print(f"{self._shade_count} shade")

    def __init__(self, name: str, height: float,
                 age: int, trunk: float) -> None:
        super().__init__(name, height, age)
        self.trunk = trunk
        self._stats = Tree._Stats()

    def show(self) -> None:
        super().show()
        print(f"Trunk diameter: {self.trunk}cm")

    def produce_shade(self) -> None:
        print(f"[asking the {self.name} to produce shade]")
        print(f"Tree {self.name} now produces a shade of "
              f"{self.height}cm long and {self.trunk}cm wide.")
        self._stats.increment_shade()


class Seed(Flower):
    def __init__(self, name: str, height: float, age: int, color: str) -> None:
        super().__init__(name, height, age, color)
        self.seed = 0

    def show(self) -> None:
        super().show()
        print(f"Seeds: {self.seed}")

    def bloom_flower(self) -> None:
        print(f"[make the {self.name} to grow, age, and bloom]")
        self.bloom = True
        self.height += 25
        self.age += 7
        self.seed += 1000
        self._stats.increment_grow()
        self._stats.increment_age()


def show_stat(plant: Plant) -> None:
    print(f"[statitics for {plant.name}]")
    plant._stats.stat_display()


if __name__ == "__main__":
    print("=== Garden statistics ===")
    print("=== Check year-old")
    Plant.check_year(30)
    Plant.check_year(400)
    print()
    print("=== Flower")
    rose = Flower("Rose", 15.0, 10, "red")
    rose.show()
    show_stat(rose)
    rose.bloom_flower()
    rose.show()
    show_stat(rose)
    print()
    print("=== Tree")
    oak = Tree("Oak", 1153.0, 873, 152.0)
    oak.show()
    show_stat(oak)
    oak.produce_shade()
    show_stat(oak)
    print()
    print("== Seed")
    sunflower = Seed("SunFlower", 200.0, 43, "yello")
    sunflower.show()
    sunflower.bloom_flower()
    sunflower.show()
    show_stat(sunflower)
    print()
    print("=== Anonymous")
    temp_plant = Plant.anonymous_plant()
    temp_plant.show()
    show_stat(temp_plant)
