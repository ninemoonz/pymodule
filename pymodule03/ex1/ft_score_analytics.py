import sys


class ScoreError(Exception):
    def __init__(self, message: str):
        super().__init__(message)
        self.message = message


class NoArgError(ScoreError):
    def __init__(self, message: str):
        super().__init__(message)
        self.message = message


class NonNumericError(ScoreError):
    def __init__(self, message: str):
        self.message = message
        super().__init__(message)


def no_arg_test(arg_list: list) -> list:
    if len(arg_list) < 2:
        raise NoArgError("No Scores Provided")
    return arg_list


def non_numeric_test(arg: str) -> list:
    if not int(arg):
        raise NonNumericError(f"Invalid parameter:\'{arg}\'")
    return arg


def score_process(arg_list: list) -> list:
    score_list: list = []
    try:
        no_arg_test(arg_list)
    except NoArgError as e:
        print(f"{e}. Usage: python3 ft_score_analytics.py <score1> <score2> ...")

    for i in range(1, len(arg_list)):
        try:
            non_numeric_test(arg_list[i])
        except ScoreError as e:
            print(f"{e}")
        else:
            score_list.append(arg_list[i])


if __name__ == "__main__":
    arg_list = sys.argv
    processed_list = score_process(arg_list)
