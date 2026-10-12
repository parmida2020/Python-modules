class Plant:
    def __init__(self, name: str, height: float,
                 age: int, growth: float) -> None:
        self.name = name
        self.height = height
        self.age = age
        self.growth = growth

    def Age(self) -> None:
        self.age += 1

    def grow(self) -> None:
        self.height = round(self.height + self.growth, 2)

    def show(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.age} days old")


def ft_plant_factory() -> None:
    print("=== Plant Factory Output ===")
    rose = Plant("Rose", 25.5, 30, 1.5)
    oak = Plant("Oak", 200, 365, 2.5)
    cactus = Plant("Cactus", 5.2, 90, 1.1)
    sunflower = Plant("Sunflower", 75.8, 46, 1.8)
    fern = Plant("Fern", 15, 120, 1.9)
    plants = [rose, oak, cactus, sunflower, fern]
    for plant in plants:
        print("Created: ", end="")  # to prevent going to the next line
        plant.show()


if __name__ == "__main__":
    ft_plant_factory()
