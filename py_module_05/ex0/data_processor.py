from abc import ABC, abstractmethod
from typing import Any


class DataProcessor(ABC):
    def __init__(self) -> None:
        self._stored: list[tuple[int, str]] = []
        self._rank: int = 0

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    @abstractmethod
    def ingest(self, data: Any) -> None:
        pass

    def output(self) -> tuple[int, str]:
        return self._stored.pop(0)


class NumericProcessor(DataProcessor):
    def validate(self, test_data: Any) -> bool:
        if isinstance(test_data, (int, float)):
            return True
        if isinstance(test_data, list):
            for element in test_data:
                if not isinstance(element, (int, float)):
                    return False
            return True
        return False

    def ingest(self, test_data: int | float | list[int | float]) -> None:
        if not self.validate(test_data):
            raise ValueError("Improper numeric data")
        else:
            if isinstance(test_data, (int, float)):
                self._stored.append((self._rank, str(test_data)))
                self._rank += 1
            if isinstance(test_data, list):
                for element in test_data:
                    self._stored.append((self._rank, str(element)))
                    self._rank += 1


class TextProcessor(DataProcessor):
    def validate(self, test_data: Any) -> bool:
        if isinstance(test_data, str):
            if test_data.isnumeric():
                return False
            return True
        if isinstance(test_data, list):
            for element in test_data:
                if not isinstance(element, str):
                    return False
            return True
        return False

    def ingest(self, test_data: str | list[str]) -> None:
        if not self.validate(test_data):
            raise ValueError("Improper numeric data")
        else:
            if isinstance(test_data, str):
                self._stored.append((self._rank, test_data))
                self._rank += 1
            if isinstance(test_data, list):
                for element in test_data:
                    self._stored.append((self._rank, element))
                    self._rank += 1


class LogProcessor(DataProcessor):
    def validate(self, test_data: Any) -> bool:
        if isinstance(test_data, dict):
            return True
        if isinstance(test_data, list):
            for element in test_data:
                if not isinstance(element, dict):
                    return False
            return True
        return False

    def ingest(self, test_data: dict[str, str] | list[dict[str, str]]) -> None:
        if not self.validate(test_data):
            raise ValueError("Improper numeric data")
        dict_values = test_data if isinstance(test_data, list) else [test_data]
        for element in dict_values:
            line: str = ": ".join(element.values())
            self._stored.append((self._rank, line))
            self._rank += 1


if __name__ == "__main__":
    print("=== Code Nexus - Data Processor ===\n")
    num_list: list[int | float] = [1, 2, 3, 4, 5]
    num_test = NumericProcessor()
    print(f"Trying to validate input '42': {num_test.validate(42)}")
    print(f"Trying to validate input 'Hello': {num_test.validate('Hello')}")
    print("Test invalid ingestion of string 'foo' without prior validation:")
    try:
        num_test.ingest('foo')
    except ValueError as e:
        print(f"Got exception: {e}")
    print(f"Processing data: {num_list}")
    num_test.ingest(num_list)
    print("Extracting 3 values...")
    for i in range(3):
        rank, value = num_test.output()
        print(f"Numeric value {rank}: {value}")
    print()
    print("Testing Text processor")
    str_test = TextProcessor()
    str_list: list[str] = ['Hello', 'Nexus', 'World']
    print(f"Trying to validate input '42': {str_test.validate('42')}")
    str_test.ingest(str_list)
    print("Processing data: ['Hello', 'Nexus', 'World']")
    print("Extracting 1 value...")
    for i in range(1):
        rank, value = str_test.output()
        print(f"Text value {rank}: {value}")
    print()
    print("Testing Log Processor...")
    dict_test = LogProcessor()
    dict_obj = [{'log_level': 'NOTICE', 'log_message': 'Connection to server'},
                {'log_level': 'ERROR', 'log_message': 'Unauthorized access!!'}]
    print(f"Trying to validate input 'Hello': {dict_test.validate('hello')}")
    print(f"Processing data: {dict_obj}")
    dict_test.ingest(dict_obj)
    print("Extracting 2 values...")
    for i in range(2):
        rank, value = dict_test.output()
        print(f"Log entry {rank}: {value}")
