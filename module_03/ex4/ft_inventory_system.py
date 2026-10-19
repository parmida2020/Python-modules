import sys


def main() -> None:
    inventory: dict[str, int] = {}
    for args in sys.argv[1:]:
        if ":" not in args:
            print(f"Error - invalid parameter '{args}'")
            continue
        key, value = args.split(":", 1)
        if not key or not value:  # empty keys and values
            print(f"Error - invalid parameter '{args}'")
            continue
        try:  # numeric-only keys
            int(key)
            print(f"Error - invalid parameter '{args}'")
            continue
        except ValueError:
            pass
        if key in inventory:  # duplicate names
            print(f"Redundant item '{key}' - discarding")
            continue
        try:
            quantity = int(value)
        except ValueError as e:  # value is not an int
            print(f"Quantity error for '{key}': {e}")
            continue
        if int(value) < 0:  # negative numbers for values
            print(f"Error - negative quantity for {key}")
            continue
        inventory[key] = quantity
    if inventory == {}:
        print("!! INVENTORY IS EMPTY")
        return
    print(f"Got inventory: {inventory}")
    print(f"Item list: {list(inventory.keys())}")
    total = sum(inventory.values())
    print(
            f"Total quantity of the {len(inventory)} items:"
            f" {total}"
        )
    if total > 0:  # avoid ZeroDivisionError
        for item in inventory.keys():
            percentage = ((inventory[item] / total) * 100)
            print(f"Item {item} represents {round(percentage, 1)}%")
    items = list(inventory.keys())
    most = items[0]
    least = items[0]
    for item in items[1:]:
        if inventory[item] > inventory[most]:
            most = item
        if inventory[item] < inventory[least]:
            least = item
    print(f"Item most abundant: {most} with quantity {inventory[most]}")
    print(f"Item least abundant: {least} with quantity {inventory[least]}")
    inventory.update({"magic_item": 1})
    print(f"Updated inventory: {inventory}")


if __name__ == "__main__":
    print("=== Inventory System Analysis ===")
    main()
