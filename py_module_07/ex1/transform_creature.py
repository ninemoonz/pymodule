from ex0.creature_abc import Creature
from .transform_cap import TransformCapability


class Shiftling(Creature, TransformCapability):
    def __init__(self) -> None:
        Creature.__init__(self, "Shiftling", "Normal")
        TransformCapability.__init__(self)

    def attack(self) -> str:
        if self._form == 0:
            return f"{self.name} attack normally."
        if self._form == 1:
            return f"{self.name} performs a boosted strike!"

    def transform(self) -> str:
        self._form = 1
        return f"{self.name} shifts into a sharper form!"

    def revert(self) -> str:
        self._form = 0
        return f"{self.name} returns to normal."


class Morphagon(Creature, TransformCapability):
    def __init__(self) -> None:
        Creature.__init__(self, "Morphagon", "Normal/Dragon")
        TransformCapability.__init__(self)

    def attack(self) -> str:
        if self._form == 0:
            return f"{self.name} attacks normally."
        if self._form == 1:
            return f"{self.name} unleashes a devastating morph strike!"

    def transform(self) -> str:
        self._form = 1
        return f"{self.name} morphs into a dragonic battle form!"

    def revert(self) -> str:
        self._form = 0
        return f"{self.name} stabilizes its form."
