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


if __name__ == "__main__":
    match_a = [(FlameFactory(), NormalStrategy()),
               (HealingCreatureFactory(), DefensiveStrategy())]
    print("Tournament 0 (basic)")
    print("[ (Flameling+Normal), (Healing+Defensive) ]")
    battle(match_a)
    print()
    match_b = [(FlameFactory(), AggressiveStrategy()),
               (HealingCreatureFactory(), DefensiveStrategy())]
    print("Tournament 1 (error)")
    print("[ (Flameling+Aggressive), (Healing+Defensive) ]")
    battle(match_b)
    print()
    match_c = [(AquaFactory(), NormalStrategy()),
               (HealingCreatureFactory(), DefensiveStrategy()),
               (TransformCreatureFactory(), AggressiveStrategy())]
    print("Tournament 2 (multiple)")
    print("[ (Aquabub+Normal), (Healing+Defensive), (Transform+Aggressive) ]")
    battle(match_c)
    print()
