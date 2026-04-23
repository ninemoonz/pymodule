import random


class Player:
    def __init__(self, name: str):
        self.name = name
        self.achievements = set()


def gen_player_achievements(player: Player, ach_list: list) -> Player:
    ach_num = random.randint(3, 10)

    for _ in range(ach_num):
        player.achievements.add(random.choice(ach_list))
    return player


if __name__ == "__main__":
    achievements: list = ["bull-dozer", "defender", "speed-runner",
                          "sniper", "joker", "street fighter",
                          "traveler", "bulls-eye", "carnivore",
                          "psychic", "gambler", "collector",
                          "berserk", "wizard", "smart one",
                          "avenger", "conqueror", "mad scientist"]

    dominic = Player("Dominic")
    sushi = Player("Sushi")
    link = Player("Link")
    mario = Player("Mario")

    player_list = [dominic, sushi, link, mario]

    print("=== Achievement Tracker System ===")
    print()
    for player in player_list:
        gen_player_achievements(player, achievements)
        print(f"Player {player.name}: {player.achievements}")
    print()
    print(f"All distinct achievements: {set.union(dominic.achievements,
                                                  sushi.achievements,
                                                  link.achievements,
                                                  mario.achievements)}")
    print()
    print(f"Common achievements: {set.intersection(dominic.achievements,
                                                   sushi.achievements,
                                                   link.achievements,
                                                   mario.achievements)}")
    print()
    for player in player_list:
        others = []
        for p in player_list:
            if p != player:
                others.append(p.achievements)
        print(f"Only {player.name} has: "
              f"{player.achievements.difference(*others)}")
    print()
    for player in player_list:
        print(f"{player.name} is missing: "
              f"{set(achievements).difference(player.achievements)}")
