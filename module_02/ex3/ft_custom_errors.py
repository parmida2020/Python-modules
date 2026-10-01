class GardenError(Exception):
    def __init__(self, message: str = "Unknown garden error") -> None:
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self, message: str = "Unknown garden error") -> None:
        super().__init__(message)


class WaterError(GardenError):
    def __init__(self, message: str = "Unknown garden error") -> None:
        super().__init__(message)


def water_plant_error() -> None:
    raise PlantError("The tomato plant is wilting!")


def water_tank_error() -> None:
    raise WaterError("Not enough water in the tank!")


def test_errors() -> None:
    print("=== Custom Garden Errors Demo ===\n")
    print("Testing PlantError...")
    try:
        water_plant_error()
    except PlantError as e:
        print(f"Caught PlantError: {e}")
    print("\nTesting WaterError...")
    try:
        water_tank_error()
    except WaterError as e:
        print(f"Cought WaterError: {e}")
    print("\nTesting catching all garden errors...")
    for func in [water_plant_error, water_tank_error]:
        try:
            func()
        except GardenError as e:
            print(f"Caught GardenError: {e}")
    print("\nAll custom error types work correctly!")


if __name__ == "__main__":
    test_errors()
