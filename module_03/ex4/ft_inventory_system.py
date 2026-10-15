import sys


def main() -> None:
    my_dict: dict = {}
    for args in sys.argv[1:]:
        if ":" not in args:
            print(f"Error - invalid parameter '{args}'")
            continue
        key, value = args.split(":", 1)
        if not key or not value:
            print(f"Error - invalid parameter '{args}'")
            continue
        if key in my_dict.keys():
            print(f"Redundant item '{key}' - discarding")
            continue
        try:
            my_dict[key] = int(value)
        except ValueError as error:
            print(f"Quantity error for '{key}': {error} ")
    if my_dict == {}:
        print("!! INVENTORY IS EMPTY")
        return
    print(f"Got inventory: {my_dict}")
    print(f"Item list: {list(my_dict.keys())}")
    total = sum(my_dict.values())
    print(
            f"Total quantity of the {len(my_dict)} items:"
            f" {total}"
        )
    if total > 0:
        for item in my_dict.keys():
            percentage = ((my_dict[item] / total) * 100)
            print(f"Item {item} represents {round(percentage, 1)}%")
    items = list(my_dict.keys())
    most = items[0]
    least = items[0]
    for item in items[1:]:
        if my_dict[item] > my_dict[most]:
            most = item
        if my_dict[item] < my_dict[least]:
            least = item
    print(f"Item most abundant: {most} with quantity {my_dict[most]}")
    print(f"Item least abundant: {least} with quantity {my_dict[least]}")
    my_dict.update({"magic_item": 1})
    print(f"Updated inventory: {my_dict}")


if __name__ == "__main__":
    print("=== Inventory System Analysis ===")
    main()
