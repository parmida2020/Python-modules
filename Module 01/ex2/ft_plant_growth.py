class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age
    def show(self) ->None:
        print(f"{self.name}: {self.height}cm, {self.age} days old")

def ft_plant_growth() ->None:
    print("=== Garden Plant Growth ===")
    flower = Plant("Lily", 45, 12)
    def age() ->None:
        for i in range(1, 8):
            print(f"=== Day {i} ===")
        def grow() ->None:
    age(1)

if __name__ == "__main__":
    ft_plant_growth()