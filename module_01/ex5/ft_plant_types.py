class Plant:
    def __init__(self, name: str, height: float, age: int):
        self.name = name
        self.height = height
        self.age = age
    def show(self):
        print(f"{self.name}: {self.height}cm, {self.age} days old")
class Flower(Plant):
    def __init__(self, name, height, age, color):
        super().__init__(name, height, age)
        self.color = color
        self.bloomed = False
    def show(self):
        super().show()
        print(f" Color: {self.color}")
    def bloom(self):
        if self.bloomed == False:
            print(f"{self.name} has not bloomed yet")
            print(f"[asking the {self.name} to bloom]")
            return
        else:
            print(f"{self.name} is blooming beautifully!")
class Tree(Plant):
    def __init__(self, name, height, age, trunk_diameter):
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter
    def show(self):
        super().show()
        print(f"{}")