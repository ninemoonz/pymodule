class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

    def show(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.age} days old")


if __name__ == "__main__":
    plant1 = Plant("Rose", 25, 23)
    plant2 = Plant("Turlip", 22, 45)
    plant3 = Plant("Iris", 23, 13)

    print("=== Garden Plant Registry ===")
    plant1.show()
    plant2.show()
    plant3.show()
