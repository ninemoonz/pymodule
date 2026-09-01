import random


NAME_LIST = ['Geralt', 'madara', 'Link', 'jin', 'Peter',
             'deku', 'Baki', 'gojo', 'jojo']


def cap_name(name_list: list[str]) -> list[str]:
    new_list: list[str] = []
    for name in name_list:
        if name == name.capitalize():
            pass
        else:
            name = name.capitalize()
        new_list.append(name)
    return new_list


def only_capped(name_list: list[str]) -> list[str]:
    new_list: list[str] = []
    for name in name_list:
        if name == name.capitalize():
            new_list.append(name)
        else:
            pass
    return new_list


def score_dict(name_list: list[str]) -> dict[str, int]:
    dict_list: dict[str, int] = {}
    for name in name_list:
        score = random.randint(0, 100)
        dict_list[name] = score
    return dict_list


def average_calc(scores: dict[str, int]) -> float:
    total: int = 0
    count: int = 0
    for val in scores.values():
        total += val
        count += 1
    return round(total / count, 2)


def top_finder(dict_list: dict[str, int], avg_score: float) -> dict[str, int]:
    above_avg: dict[str, int] = {}
    for key in dict_list:
        if dict_list[key] > avg_score:
            above_avg[key] = dict_list[key]
    return above_avg


if __name__ == "__main__":
    all_cap = cap_name(NAME_LIST)
    only_cap = only_capped(NAME_LIST)
    print(f"New list with all names capitalized: {all_cap}")
    print(f"New list of capitalized names only: {only_cap}")
    print()
    dict_list = score_dict(all_cap)
    print(dict_list)
    average_score = average_calc(dict_list)
    print(f"Score average is {average_score}")
    above_avg = top_finder(dict_list, average_score)
    print(f"High scores: {above_avg}")
