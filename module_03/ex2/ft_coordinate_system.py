import math


def get_player_pos() -> tuple[float, float, float]:
    while True:
        coordinates = input("Enter new coordinates as"
                            " floats in format 'x,y,z': ")
        parts = coordinates.split(",")
        if len(parts) != 3:
            print("Invalid syntax")
            continue  # skip the rest code and goes back -> next iteration
        values: list[float] = []  # create an empty list -> values inside
        valid = True
        for part in parts:
            try:
                values += [float(part)]
            except ValueError as e:
                print(f"Error on parameter '{part}': {e}")
                valid = False
                break
        if valid:  # we want to make sure that all the 3 values are valid
            return (values[0], values[1], values[2])  # tuple


if __name__ == "__main__":
    print("=== Game Coordinate System ===\n")
    print("Get a first set of coordinates")
    try:
        temp = get_player_pos()
        x, y, z = temp
        print(f"Got a first tuple: {temp}")
        print(f"It includes: X={x}, Y={y}, Z={z}")
        dis1 = round(math.sqrt((x**2) + (y**2) + (z**2)), 4)
        print(f"Distance to center: {dis1}\n")
        print("Get a second set of coordinates")
        temp2 = get_player_pos()
        x2, y2, z2 = temp2
        dis2 = round(math.sqrt((x2-x)**2 + (y2-y)**2 + (z2-z)**2), 4)
        print(f"Distance between the 2 sets of coordinates: {dis2}")
    except KeyboardInterrupt:
        print("Program terminated by user.")
