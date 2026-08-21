class Plant:
    def __init__(self, name: str, height: float, plantAge: int, growth: float) -> None:
        self.name = name
        self.height = height
        self.plantAge = plantAge
        self.growth = growth
    def age(self) ->None:
        self.plantAge += 1
    def grow(self) ->None:
        self.height = round(self.height + self.growth, 2)
    def show(self) ->None:
        print(f"{self.name}: {self.height}cm, {self.plantAge} days old")

def ft_plant_growth() ->None:
    print("=== Garden Plant Growth ===")
    flower = Plant("Lily", 45.8, 12, 1.2)
    flower.show()
    start_height = flower.height
    day = 1
    while (day < 8):
        print(f"=== Day {day} ===")
        flower.age()
        flower.grow()
        flower.show()
        day += 1
    print(f"Growth this week: {round(flower.height - start_height, 2)}cm")

if __name__ == "__main__":
    ft_plant_growth()