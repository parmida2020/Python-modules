class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        self._height = height
        self._age = age
    def show(self) ->None:
        print(f"Plant created: {self.name}: {self._height}cm, {self._age} days old")
    def get_height(self)-> float:
     return self._height
    def get_age(self)-> int:
         return self._age
    def set_height(self, height: float)-> None:
        if height < 0:
            print(f"\n{self.name}: Error, height can't be negative")
            print("Height update rejected")
            return
        self._height = height
        print(f"\nHeight updated: {height}cm")
    def set_age(self, age: int)-> None:
        if age < 0:
            print(f"{self.name}: Error, age can't be negative")
            print("Age update rejected")
            return
        self._age = age
        print(f"Age updated: {age} days")

def ft_garden_security()-> None:
    print("=== Garden Security System ===")
    flower = Plant("Rose", 15.5, 10)
    flower.show()
    flower.set_height(25)
    flower.set_age(49)
    flower.set_height(-7.56)
    flower.set_age(-10)
    print(f"\nCurrent state: {flower.name}: {flower.get_height()}cm, {flower.get_age()} days old")
    
if __name__ == "__main__":
     ft_garden_security()