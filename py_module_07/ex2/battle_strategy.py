from abc import ABC, abstractmethod


class BattleStrategy(ABC):
    @abstractmethod
    def act(self) -> None:
        ...

    @abstractmethod
    def is_valid(self) -> bool:
        ...
