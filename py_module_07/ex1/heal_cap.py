from abc import ABC, abstractmethod


class HealCapability(ABC):
    def __init__(self) -> None:
        pass

    @abstractmethod
    def heal(self, target=None) -> str:
        pass
