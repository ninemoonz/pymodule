from ex0.creature_abc import Creature
from ex1.heal_cap import HealCapability
from ex1.transform_cap import TransformCapability
from ex2.battle_strategy import BattleStrategy


class StrategyError(Exception):
    ...


class NormalStrategy(BattleStrategy):
    def act(self, creature: Creature) -> str:
        return creature.attack()

    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, Creature)


class AggressiveStrategy(BattleStrategy):
    def act(self, creature: Creature) -> str:
        if not isinstance(creature, TransformCapability):
            raise StrategyError("Battle Error, Aborting tournament:"
                                f"Invalid Creature '{creature.name}' "
                                "for this Aggressive Strategy")
        return (f"{creature.transform()}\n"
                f"{creature.attack()}\n"
                f"{creature.revert()}")

    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, TransformCapability)


class DefensiveStrategy(BattleStrategy):
    def act(self, creature: Creature) -> str:
        if not isinstance(creature, HealCapability):
            raise StrategyError("Battle Error, Aborting tournament:"
                                f"Invalid Creature '{creature.name}' "
                                "for this Defensive Strategy")
        return f"{creature.attack()}\n{creature.heal()}"

    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, HealCapability)
