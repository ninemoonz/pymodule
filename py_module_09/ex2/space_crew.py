from pydantic import BaseModel, model_validator, Field, ValidationError
from enum import Enum


class Rank(Enum):
    CADET = "cadet"



if __name__ == "__main__":
    print("hello world")
