class Plant:
    def __init__(self, name: str, height: float, age: int):
        self.name = name
        self.height = height
        self.age = age

    def show(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.age} days old")


class Flower(Plant):
    def __init__(self, name, height, age, color):
        super().__init__(name, height, age)
        self.color = color
        self.bloomed = False

    def bloom(self) -> None:
        print(f"[asking the {self.name} to bloom]")
        self.bloomed = True

    def show(self) -> None:
        super().show()
        print(f" Color: {self.color}")
        if self.bloomed is False:
            print(f" {self.name} has not bloomed yet")
        else:
            print(f" {self.name} is blooming beautifully!\n")


class Tree(Plant):
    def __init__(self, name, height, age, trunk_diameter):
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self) -> None:
        print(f"[asking the {self.name} to produce shade]")
        print(
              f"Tree {self.name.lower()} now produces a shade of {self.height}"
              f"cm long and {self.trunk_diameter}cm wide.\n"
        )

    def show(self) -> None:
        super().show()
        print(f" Trunk diameter: {self.trunk_diameter}")


class Vegetable(Plant):
    def __init__(self, name, height, age, harvest_season):
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = 0

    def grow(self) -> None:
        self.height += 1

    def age_up(self) -> None:
        self.age += 1
        self.nutritional_value += 1

    def show(self) -> None:
        super().show()
        print(f" Harvest season: {self.harvest_season}")
        print(f" Nutritional value: {self.nutritional_value}")


def ft_plant_types() -> None:
    print("=== Garden Plant Types ===")
    rose = Flower("Rose", 15.0, 14, "pink")
    oak = Tree("Oak", 200.0, 365, 5.0)
    tomato = Vegetable("Tomato", 5.0, 10, "september")
    print("=== Flower")
    rose.show()
    rose.bloom()
    rose.show()
    print("=== Tree")
    oak.show()
    oak.produce_shade()
    print("=== Vegeteble")
    tomato.show()
    print(f"[make {tomato.name.lower()} grow and age for 20 days]")
    for i in range(20):
        tomato.grow()
        tomato.age_up()
    tomato.show()


if __name__ == "__main__":
    ft_plant_types()
