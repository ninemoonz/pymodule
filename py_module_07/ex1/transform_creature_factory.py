from ex0.creature_abc import Creature
from ex0.creature_factory import CreatureFactory
from .transform_creature import Shiftling, Morphagon


class TransformCreatureFactory(CreatureFactory):
    def create_base(self) -> Creature:
        return Shiftling()

    def create_evolved(self) -> Creature:
        return Morphagon()
