import random
players = ["Alice", "bob", "Charlie", "dylan", "Emma",
           "Gregory", "john", "kevin", "Liam"]


def main() -> None:
    print("=== Game Data Alchemist ===\n")
    print(f"Initial list of players: {players}")
    newlist = [player.capitalize() for player in players]
    print(f"New list with all names capitalized: {newlist}")
    new_list = [p for p in players if p == p.capitalize()]
    print(f"New list of capitalized names only: {new_list}\n")
    new_dict = {player: random.randint(1, 1000) for player in newlist}
    print(f"Score dict: {new_dict}")
    total = 0
    for player in new_dict:
        total += new_dict[player]
    average = round((total / len(new_dict)), 2)
    print(f"Score average is {average}")
    high_score = {p: new_dict[p] for p in new_dict if new_dict[p] > average}
    print(f"High scores: {high_score}")


if __name__ == "__main__":
    main()
