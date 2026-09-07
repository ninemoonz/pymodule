from itertools import combinations
from typing import List, Tuple
from ex0 import CreatureFactory, FlameFactory, AquaFactory
from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex2 import (BattleStrategy,
                 NormalStrategy,
                 AggressiveStrategy,
                 DefensiveStrategy,
                 StrategyError)


Opponent = Tuple[CreatureFactory, BattleStrategy]


def battle(opponents: List[Opponent]) -> None:
    print("*** Tournament ***")
    print(f"{len(opponents)} opponents involved")
    print()
    fighters = [
        (factory.create_base(), strategy) for factory, strategy in opponents
    ]
    for (creature_a, strategy_a), (creature_b, strategy_b) in combinations(fighters, 2):
        print("* Battle *")
        print(creature_a.describe())
        print(" vs. ")
        print(creature_b.describe())
        print(" Now Fight!")
        try:
            print(strategy_a.act(creature_a))
            print(strategy_b.act(creature_b))
        except StrategyError as e:
            print(f"Battle Error, aborting tournament: {e}")
            return
        print()


if __name__ == "__main__":
    match_a = ((FlameFactory(), NormalStrategy()),
               (HealingCreatureFactory(), DefensiveStrategy()))
    print("Tournament 0 (basic)")
    battle(match_a)
    print()
    match_b = ((FlameFactory(), AggressiveStrategy()),
               (HealingCreatureFactory(), DefensiveStrategy()))
    print("Tournament 1 (error)")
    battle(match_b)
    print()
    match_c = ((AquaFactory(), NormalStrategy()),
               (HealingCreatureFactory(), DefensiveStrategy()),
               (TransformCreatureFactory(), AggressiveStrategy()))
    battle(match_c)
    print()
