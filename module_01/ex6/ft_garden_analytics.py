class Plant:
    class Statics:
        def __init__(self):
            self.grow_count = 0
            self.age_count = 0
            self.show_count = 0

        def add_grow(self) -> None:
            self.grow_count += 1

        def add_age(self) -> None:
            self.age_count += 1

        def add_show(self) -> None:
            self.show_count += 1

        def display(self) -> None:
            print(f"[statistics for {self.name}]")
            print(
                f"Stats: {self.grow_count} grow, {self.age_count} age, "
                f" {self.show_count} show"
            )

    @staticmethod
    def check_year(age) -> bool:
        return age > 365

    @classmethod
    def annonymous_plant(cls):
        return cls("Unknown plant", 0.0, 0)

    def __init__(self, name: str, height: float, age: int):
        self.name = name
        self.height = height
        self.age = age
        self.statics = Plant.Statics()

    def grow(self) -> None:
        self.height += 1
        self._stats.add_grow()

    def age_up(self) -> None:
        self.age += 1
        self._stats.add_age()

    def show(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.age} days old")


class Flower(Plant):
    def __init__(self, name, height, age, color,
                 grow_count, age_count, show_count):
        super().__init__(name, height, age)
        self.color = color
        self.bloomed = False
        self.grow_count = grow_count
        self.age_count = age_count
        self.show_count = show_count

    def bloom(self) -> None:
        print(f"[asking the {self.name} to bloom]")
        self.bloomed = True

    def show(self) -> None:
        super().show()
        self.show_count += 1
        print(f" Color: {self.color}")


class Tree(Plant):
    def __init__(self, name, height, age, trunk_diameter):
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self) -> None:
        print("[asking the oak to produce shade]")
        print(
            f"Tree {self.name} now produces a shade of {self.height} long "
            f"and {self.trunk_diameter}cm wide."
        )

    def show(self) -> None:
        super().show()
        print(f" Trunk diameter: {self.trunk_diameter}")


def ft_garden_analytics() -> None:
    print("=== Garden statistics ===")
    print("=== Check year-old")
    print(f"Is 30 days more than a year? -> {Plant.check_year(30)}")
    print(f"Is 400 days more than a year? -> {Plant.check_year(400)}\n")
    rose = Flower("Rose", 15.0, 14, "pink")
    oak = Tree("Oak", 200.0, 365, 5.0)
    print("=== Flower")
    rose.show()
    rose.bloom()
    rose.show()
    print("=== Tree")
    oak.show()
    oak.produce_shade()
    print("=== Anonymous")


if __name__ == "__main__":
    ft_garden_analytics()
