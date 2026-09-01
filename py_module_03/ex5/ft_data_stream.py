import typing
import random


RAND_NAME = ['Rick', 'Morty', 'Cartman', 'Kenny', 'Kyle', 'Stan']
RAND_ACTION = ['sit', 'jump', 'kick', 'yell',
               'punch', 'run', 'walk', 'look', 'laugh']


def gen_event(name_list: list[str],
              action_list: list[str],
              ) -> typing.Generator[tuple[str, str], None, None]:
    while True:
        key_name: str = random.choice(name_list)
        value_action: str = random.choice(action_list)
        pair_tup: tuple[str, str] = (key_name, value_action)
        yield pair_tup


def consume_event(ten_list: list[tuple[str, str]],
                  ) -> typing.Generator[tuple[str, str], None, None]:
    while ten_list:
        i = random.randrange(len(ten_list))
        print(f"Got event from list: {ten_list[i]}")
        rand_event: tuple[str, str] = ten_list.pop(i)
        yield rand_event


if __name__ == "__main__":
    event = gen_event(RAND_NAME, RAND_ACTION)
    new_list: list[tuple[str, str]] = []
    print("=== Game Data Stream Processor ===")
    for i in range(1000):
        event_pair = next(event)
        print(f"Event {i}: Player {event_pair[0]} did action {event_pair[1]}")
        new_list.append(event_pair)

    ten_list = [next(event) for _ in range(10)]
    print(f"Built list of 10 list {ten_list}")

    for consumed in consume_event(ten_list):
        print(f"Remains in list: {ten_list}")
