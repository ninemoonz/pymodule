from pydantic import BaseModel, model_validator, Field, ValidationError
from data_generator import CrewMissionGenerator, DataConfig
from datetime import datetime
from enum import Enum


class Rank(Enum):
    CADET = "cadet"
    OFFICER = "officer"
    LIEUTENANT = "lieutenant"
    CAPTAIN = "captain"
    COMMANDER = "commander"


class CrewMember(BaseModel):
    member_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=2, max_length=50)
    rank: Rank
    age: int = Field(ge=18, le=80)
    specialization: str = Field(min_length=3, max_length=30)
    years_experience: int = Field(ge=0, le=50)
    is_active: bool = Field(default=True)


class SpaceMission(BaseModel):
    mission_id: str = Field(min_length=5, max_length=15)
    mission_name: str = Field(min_length=3, max_length=100)
    destination: str = Field(min_length=3, max_length=50)
    launch_date: datetime
    duration_days: int = Field(ge=1, le=3650)
    crew: list[CrewMember] = Field(min_length=1, max_length=12)
    mission_status: str = Field(default="planned")
    budget_millions: float = Field(ge=1.0, le=10000.0)

    @model_validator(mode='after')
    def mission_validation(self) -> 'SpaceMission':
        if self.mission_id[:1] != 'M':
            raise ValueError("Mission ID should start with letter 'M'.")
        high_officer = False
        for member in self.crew:
            if member.rank == Rank.COMMANDER or member.rank == Rank.CAPTAIN:
                high_officer = True
                break
        if not high_officer:
            raise ValueError("Mission must have at least one "
                             "Commander or Captain.")
        experience = 0
        mem_num = len(self.crew)
        for member in self.crew:
            if member.years_experience >= 5:
                experience += 1
        if experience < mem_num * 0.5:
            raise ValueError(f"This mission need at least {mem_num * 0.5} "
                             "crews with 5+ years of experiences.")
        for member in self.crew:
            if not member.is_active:
                raise ValueError("All crew member must be active.")
        return self


def main() -> None:
    # Generate mission data
    config = DataConfig()
    generator = CrewMissionGenerator(config)
    raw_missions = generator.generate_mission_data(count=3)
    raw_mission = raw_missions[0]

    print("Space Mission Crew Validation")
    print("=============================")
    for raw in raw_missions:
        try:
            print("Valid mission created:")
            mission = SpaceMission(**raw)
            print(f"Mission: {mission.mission_name}")
            print(f"ID: {mission.mission_id}")
            print(f"Destination: {mission.destination}")
            print(f"Budget: {mission.budget_millions}M")
            print(f"Crew size: {len(mission.crew)}")
            for crew in mission.crew:
                print(f"- {crew.name} ({crew.rank.value}) "
                      f"- {crew.specialization}")
            print()
        except ValidationError as e:
            for err in e.errors():
                print(f" {err['msg']}")
    print()
    print("=============================")
    print("Expected validation error:")
    try:
        bad_mission = raw_mission.copy()
        bad_mission["mission_id"] = "2314-TITAN"
        SpaceMission(**bad_mission)
        print("No Validation error detected")
    except ValidationError as e:
        for err in e.errors():
            print(f" {err['msg']}")


if __name__ == "__main__":
    main()
