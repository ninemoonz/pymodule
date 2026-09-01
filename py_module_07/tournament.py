from ex0 import CreatureFactory, FlameFactory, AquaFactory
from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex2 import NormalStrategy, AggressiveStrategy, DefensiveStrategy, StrategyError


def battle_match(match_pair: tuple[Creature, CreatureFactory]) -> None:
    print("*** Tournament ***")


if __name__ == "__main__":
    print("Tournament 0 (Basic)")
    flameling = FlameFactory().create_base()
    sproutling = HealingCreatureFactory().create_base()
    print(f"[({flameling.name}+Normal), ({sproutling.name}+Defensive)]")
    print("*** Tournament ***")
    print("2 opponents involved")
    print()
    print("* Battle *")
    print(flameling.describe())
    print("vs.")
    print(sproutling.describe())
    print("NOW FIGHT!")
    normal = NormalStrategy()
    defensive = DefensiveStrategy()
    aggresive = AggressiveStrategy()
    try:
        if normal.is_valid(flameling) and defensive.is_valid(sproutling):
            print(normal.act(flameling))
            print(defensive.act(sproutling))
    except StrategyError as e:
        print(e)
