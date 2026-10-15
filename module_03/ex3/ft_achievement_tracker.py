import random
achievements: list[str] = [
    "Crafting Genius", "Strategist", "World Savior", "Speed Runner",
    "Survivor", "Master Explorer", "Treasure Hunter", "Unstoppable",
    "First Steps", "Collector Supreme", "Untouchable", "Sharp Mind",
    "Boss Slayer", "Hidden Path Finder",
]


def gen_player_achievements() -> set[str]:
    num = random.randint(5, 10)
    selected = random.sample(list(achievements), num)
    return set(selected)


def main() -> None:
    print("=== Achievement Tracker System ===\n")
    alice = gen_player_achievements()
    bob = gen_player_achievements()
    charlie = gen_player_achievements()
    dylan = gen_player_achievements()
    all_achievements = set(achievements)
    print(f"Player Alice: {alice}\n")
    print(f"Player Bob: {bob}\n")
    print(f"Player Charlie: {charlie}\n")
    print(f"Player Dylan: {dylan}\n")
    print(f"All distinct achievements: {alice.union(bob, charlie, dylan)}\n")
    print(f"Common achievements: {alice.intersection(bob, charlie, dylan)}\n")
    # Difference between the sets
    print(f"Only Alice has: {alice.difference(bob, charlie, dylan)}")
    print(f"Only Bob has: {bob.difference(alice, charlie, dylan)}")
    print(f"Only Charlie has: {charlie.difference(bob, alice, dylan)}")
    print(f"Only Dylan has: {dylan.difference(bob, charlie, alice)}\n")
    # The missing achievement
    print(f"Alice is missing: {all_achievements.difference(alice)}\n")
    print(f"Bob is missing: {all_achievements.difference(bob)}\n")
    print(f"Charlie is missing: {all_achievements.difference(charlie)}\n")
    print(f"Dylan is missing: {all_achievements.difference(dylan)}")


if __name__ == "__main__":
    main()
