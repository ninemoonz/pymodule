from abc import ABC, abstractmethod


class TransformCapability(ABC):
    def __init__(self) -> None:
        self._form: int = 0

    @abstractmethod
    def transform(self) -> str:
        pass

    @abstractmethod
    def revert(self) -> str:
        pass
