class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

    def show(self) -> None:
        print(f"Created: {self.name}: {self.height}cm, {self.age} days old")


def ft_plant_factory() -> None:
    print("=== Plant Factory Output ===")
    rose = Plant("Rose", 25.5, 30)
    oak = Plant("Oak", 200, 365)
    cactus = Plant("Cactus", 5.2, 90)
    sunflower = Plant("Sunflower", 75.8, 46)
    fern = Plant("Fern", 15, 120)
    plants = [rose, oak, cactus, sunflower, fern]
    for plant in plants:
        plant.show()


if __name__ == "__main__":
    ft_plant_factory()
