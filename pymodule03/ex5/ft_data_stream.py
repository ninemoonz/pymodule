import typing
import random


RAND_NAME = ['Rick', 'Morty', 'Cartman', 'Kenny', 'Kyle', 'Stan']
RAND_ACTION = ['sit', 'jump', 'kick', 'yell',
               'punch', 'run', 'walk', 'look', 'laugh']


def get_event(name_list: list[str], action_list: list[str]):
    while True:
        key_name: str = random.choice(name_list)
        value_action: str = random.choice(action_list)
        pair_tup: tuple = (key_name, value_action)
        yield pair_tup


if __name__ == "__main__":
    event = get_event(RAND_NAME, RAND_ACTION)
    new_list = []
    print("=== Game Data Stream Processor ===")

    for i in range(30):
        element = next(event)
        print(f"Event {i}: Player {element[0]} did action {element[1]}")
        new_list.append(element)

    print(f"Built list of {i} events: {new_list}")
