#!/usr/bin/python3

import sys


class ScoreError(Exception):
    def __init__(self, message: str = "No Scores Provided. Usage: python3 "
                                      "ft_score_analytics.py "
                                      "<score1> <score2> ...") -> None:
        super().__init__(message)
        self.message = message


class NoArgError(ScoreError):
    pass


class NonNumericError(ScoreError):
    pass


def no_arg_test(arg_list: list[str]) -> None:
    if len(arg_list) < 2:
        raise NoArgError()


def non_numeric_test(arg: str) -> None:
    try:
        int(arg)
    except ValueError:
        raise NonNumericError(f"Invalid parameter: '{arg}'")


def score_process(arg_list: list[str]) -> list[int]:
    score_list: list[int] = []
    try:
        no_arg_test(arg_list)
    except NoArgError as e:
        print(e)
        return score_list

    for i in range(1, len(arg_list)):
        try:
            non_numeric_test(arg_list[i])
            score_list.append(int(arg_list[i]))
        except NonNumericError as e:
            print(e)

    if not score_list:
        print(ScoreError())

    return score_list


if __name__ == "__main__":
    arg_list = sys.argv
    processed_list: list[int] = []
    print("=== Player Score Analytics ===")
    processed_list = score_process(arg_list)
    if processed_list:
        total_player = len(processed_list)
        total_score = sum(processed_list)
        average_score = total_score / total_player
        high_score = max(processed_list)
        low_score = min(processed_list)
        score_range = high_score - low_score

        print(f"Scores Processed: {processed_list}")
        print(f"Total players: {total_player}")
        print(f"Total score: {total_score}")
        print(f"Average score: {average_score:.1f}")
        print(f"High score: {high_score}")
        print(f"Low score: {low_score}")
        print(f"Score range: {score_range}")
    print()
