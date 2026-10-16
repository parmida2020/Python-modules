import sys


def main() -> None:
    inventory: dict = {}
    for args in sys.argv[1:]:
        if ":" not in args:
            print(f"Error - invalid parameter '{args}'")
            continue
        key, value = args.split(":", 1)
        if not key or not value:
            print(f"Error - invalid parameter '{args}'")
            continue
        if key in inventory.keys():
            print(f"Redundant item '{key}' - discarding")
            continue
        try:
            inventory[key] = int(value)
        except ValueError as error:
            print(f"Quantity error for '{key}': {error} ")
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
    if total > 0:
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
