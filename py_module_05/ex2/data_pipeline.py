from abc import ABC, abstractmethod
from typing import Any, Protocol


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
    name = "Numeric Processor"

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
    name = "Text Processor"

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
            raise ValueError("Improper text data")
        if isinstance(test_data, str):
            self._stored.append((self._rank, test_data))
            self._rank += 1
        if isinstance(test_data, list):
            for element in test_data:
                self._stored.append((self._rank, element))
                self._rank += 1


class LogProcessor(DataProcessor):
    name = "Log Processor"

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
            raise ValueError("Improper log data")
        dict_values = test_data if isinstance(test_data, list) else [test_data]
        for element in dict_values:
            line: str = ": ".join(element.values())
            self._stored.append((self._rank, line))
            self._rank += 1


class ExportPlugin(Protocol):
    def process_output(self, data: list[tuple[int, str]]) -> None:
        ...


class CSVPlugin:
    def process_output(self, data: list[tuple[int, str]]) -> None:
        csv_str: list[str] = []
        for tup_el in data:
            csv_str.append(tup_el[1])
        join_csv = ",".join(csv_str)
        print("CSV Output:")
        print(join_csv)


class JSONPlugin:
    def process_output(self, data: list[tuple[int, str]]) -> None:
        json_list: list[str] = []
        for tup_el in data:
            key, value = tup_el
            key_name = "item_" + str(key)
            json_value = f'"{key_name}": "{value}"'
            json_list.append(json_value)
        json_str = ", ".join(json_list)
        json_result = "{" + json_str + "}"
        print("JSON Output:")
        print(json_result)


class DataStream:
    def __init__(self) -> None:
        self._proc_list: list[DataProcessor] = []

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

    def output_pipeline(self, nb: int, plugin: ExportPlugin) -> None:
        for proc in self._proc_list:
            count = min(nb, len(proc._stored))
            data = [proc.output() for _ in range(count)]
            plugin.process_output(data)


if __name__ == "__main__":
    test_data: list[Any] = ['Hello world',
                            [3.14, -1, 2.71],
                            [{'log_level': 'WARNING',
                              'log_message': 'Telnet access! Use ssh instead'},
                             {'log_level': 'INFO',
                             'log_message': 'User wil is connected'}],
                            42, ['Hi', 'five']]
    test_data_2: list[Any] = [21,
                              ['I love AI',
                               'LLMs are wonderful',
                               'Stay healthy'],
                              [{'log_level': 'ERROR',
                                'log_message': '500 server crash'},
                               {'log_level': 'NOTICE',
                                'log_message':
                                'Certificate expires in 10 days'}],
                              [32, 42, 64, 84, 128, 168],
                              'World hello']
    print("=== Code Nexus - Data Pipeline ===")
    print()
    print("Initialize Data Stream...")
    ds = DataStream()
    np = NumericProcessor()
    tp = TextProcessor()
    lp = LogProcessor()
    csv_p = CSVPlugin()
    print()
    ds.print_processors_stats()
    print()
    print("Registering Processors")
    ds.register_processor(np)
    ds.register_processor(tp)
    ds.register_processor(lp)
    print()
    print("Send first batch of data on stream")
    ds.process_stream(test_data)
    print()
    ds.print_processors_stats()
    print()
    print("Send 3 processed data from each processor to a CSV plugin:")
    ds.output_pipeline(3, csv_p)
    print()
    ds.print_processors_stats()
    print()
    print("Send another batch of data")
    ds.process_stream(test_data_2)
    print()
    ds.print_processors_stats()
    print()
    print("Send 5 processed data from each processor to JSON plugin:")
    json_p = JSONPlugin()
    ds.output_pipeline(5, json_p)
    print()
    ds.print_processors_stats()
