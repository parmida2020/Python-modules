import typing
import random

players = ["alice", "bob", "charlie", "dylan"]
actions = ["run", "eat", "sleep", "grab", "move",
           "swim", "climb", "use", "release"]


def gen_event() -> typing.Generator[tuple[str, str], None, None]:
    while True:
        name = random.choice(players)
        action = random.choice(actions)
        yield (name, action)


def consume_event(
        events: list[tuple[str, str]]
        ) -> typing.Generator[tuple[str, str], None, None]:
    while events:
        index = random.randrange(len(events))
        event = events[index]
        events[:] = events[:index] + events[index + 1:]
        yield event


def main() -> None:
    print("=== Game Data Stream Processor ===")
    event_gen = gen_event()  # to save the generator to ask for the next event
    for i in range(1000):
        name, action = next(event_gen)
        print(f"Event {i}: Player {name} did action {action}")
    events = [next(event_gen) for j in range(10)]
    print(f"Built list of 10 events: {events}")
    for event in consume_event(events):
        print(f"Got event from list: {event}")
        print(f"Remains in list: {events}")


if __name__ == "__main__":
    main()
