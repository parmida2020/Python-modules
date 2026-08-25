class Plant:
    @staticmethod
    def check_year(age):
        return age > 365
    def __init__(self, name: str, height: float, age: int):
        self.name = name
        self.height = height
        self.age = age
    def show(self) ->None:
        print(f"{self.name}: {self.height}cm, {self.age} days old")

class Flower(Plant):
    def __init__(self, name, height, age, color):
        super().__init__(name, height, age)
        self.color = color
        self.bloomed = False
    def bloom(self) ->None:
        print(f"[asking the {self.name} to bloom]")
        self.bloomed = True
    def show(self) ->None:
        super().show()
        print(f" Color: {self.color}")
        if self.bloomed == False:
            print(f" {self.name} has not bloomed yet")
        else:
            print(f" {self.name} is blooming beautifully!")
        
class Tree(Plant):
    def __init__(self, name, height, age, trunk_diameter):
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter
    def produce_shade(self) ->None:
        print("[asking the oak to produce shade]")
        print(f"Tree {self.name} now produces a shade of {self.height} long and {self.trunk_diameter}cm wide.")
    def show(self) ->None:
        super().show()
        print(f" Trunk diameter: {self.trunk_diameter}")

def ft_garden_analytics() ->None:
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
    oak.show()

if __name__ == "__main__":
    ft_garden_analytics()