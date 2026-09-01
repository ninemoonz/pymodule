class SecurePlant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self._name = name
        self._height = height
        self._age = age

    def set_height(self, height: int) -> None:
        if height < 0:
            print(f"{self._name}: Error, height can't be negative")
            print("Height update rejected")
            return
        self._height = height
        print(f"Height updated: {self._height}cm")

    def get_height(self) -> int:
        return self._height

    def set_age(self, age: int) -> None:
        if age < 0:
            print(f"{self._name}: Error, age can't be negative")
            print("Age update rejected")
            return
        self._age = age
        print(f"Age updated: {self._age} days")

    def get_age(self) -> int:
        return self._age

    def get_info(self) -> None:
        print(f"Current state: {self._name}: "
              f"{self._height}cm, {self._age} days old")


if __name__ == "__main__":
    print("=== Garden Security System ===")
    plant = SecurePlant("Rose", 15, 20)
    print(f"Plant created: {plant._name}: "
          f"{plant.get_height()}cm, {plant.get_age()} days old")
    print()
    plant.set_height(25)
    plant.set_age(30)
    plant.get_height()
    plant.get_age()
    print()
    plant.set_height(-10)
    plant.set_age(-2)
    print()
    plant.get_info()
