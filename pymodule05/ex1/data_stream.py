from abc import ABC, abstractmethod
from typing import Any


class DataProcessor(ABC):
    name: str

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
    name: str = "Numeric Processor"

    def validate(self, test_data: Any) -> bool:
        if isinstance(test_data, (int, float)):
            return True
        if isinstance(test_data, list):
            for element in test_data:
                if not isinstance(element, (int, float)):
                    return False
            return True
        return False

    def ingest(self, test_data: Any) -> None:
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
    name: str = "Text Processor"

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

    def ingest(self, test_data: Any) -> None:
        if not self.validate(test_data):
            raise ValueError("Improper numeric data")
        if isinstance(test_data, str):
            self._stored.append((self._rank, test_data))
            self._rank += 1
        if isinstance(test_data, list):
            for element in test_data:
                self._stored.append((self._rank, element))
                self._rank += 1


class LogProcessor(DataProcessor):
    name: str = "Log Processor"

    def validate(self, test_data: Any) -> bool:
        if isinstance(test_data, dict):
            return True
        if isinstance(test_data, list):
            for element in test_data:
                if not isinstance(element, dict):
                    return False
            return True
        return False

    def ingest(self, test_data: Any) -> None:
        if not self.validate(test_data):
            raise ValueError("Improper numeric data")
        dict_values = test_data if isinstance(test_data, list) else [test_data]
        for element in dict_values:
            line: str = ": ".join(element.values())
            self._stored.append((self._rank, line))
            self._rank += 1


class DataStream():
    def __init__(self):
        self._proc_list = []

    def register_processor(self, proc: DataProcessor) -> None:
        self._proc_list.append(proc)

    def process_stream(self, stream: list[Any]) -> None:
        for item in stream:
            item_valid: bool = False
            for proc in self._proc_list:
                if proc.validate(item):
                    proc.ingest(item)
                    item_valid = True
                    break
            if not item_valid:
                print("DataStream Error - "
                      f"Can't process element in stream: {item}")

    def print_processors_stats(self) -> None:
        print("== DataStream Statistics ==")
        if len(self._proc_list) == 0:
            print("No processor found, no data")
            return
        for proc in self._proc_list:
            print(f"{proc.name}: total {proc._rank} items processed, "
                  f"remaining {len(proc._stored)} on processor")


if __name__ == "__main__":
    test_data: list[Any] = ['Hello world',
                            [3.14, -1, 2.71],
                            [{'log_level': 'WARNING',
                              'log_message': 'Telnet access! Use ssh instead'},
                             {'log_level': 'INFO',
                             'log_message': 'User wil is connected'}],
                            42, ['Hi', 'five']]
    print("=== Code Nexus - Data Stream ===")
    poly_obj = DataStream()
    poly_obj.print_processors_stats()
    print()
    print("Registering Numeric Processor")
    num_proc = NumericProcessor()
    poly_obj.register_processor(num_proc)
    print("Send first batch of data on stream")
    poly_obj.process_stream(test_data)
    poly_obj.print_processors_stats()
    print()
    print("Registering other data processors")
    txt_obj = TextProcessor()
    log_obj = LogProcessor()
    poly_obj.register_processor(txt_obj)
    poly_obj.register_processor(log_obj)
    print("Send same batch again")
    poly_obj.process_stream(test_data)
    poly_obj.print_processors_stats()
    print()
    print("Consume some elements from the data processors: Numeric 3, Text 2, Log 1")
    for i in range(3):
        num_proc.output()
    for i in range(2):
        txt_obj.output()
    log_obj.output()
    poly_obj.print_processors_stats()
