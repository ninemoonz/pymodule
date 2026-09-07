from ex0.creature_factory import CreatureFactory
from .transform_creature import Shiftling, Morphagon


class TransformCreatureFactory(CreatureFactory):
    def create_base(self) -> Shiftling:
        return Shiftling()

    def create_evolved(self) -> Morphagon:
        return Morphagon()
