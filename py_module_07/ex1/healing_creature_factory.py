from ex0 import CreatureFactory
from ex0.creature_abc import Creature
from .heal_creature import Sproutling, Bloomelle


class HealingCreatureFactory(CreatureFactory):
    def create_base(self) -> Creature:
        return Sproutling()

    def create_evolved(self) -> Creature:
        return Bloomelle()
