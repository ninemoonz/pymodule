from pydantic import BaseModel, Field, ValidationError
from datetime import datetime
from typing import Optional


class SpaceStation(BaseModel):
    station_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=1, max_length=50)
    crew_size: int = Field(ge=1, le=20)
    power_level: float = Field(multiple_of=0.1, ge=0.0, le=100.0)
    oxygen_level: float = Field(multiple_of=0.1, ge=0.0, le=100.0)
    last_maintenance: datetime
    is_operational: bool = Field(default=True)
    notes: Optional[str] = Field(default=None, max_length=200)


def main() -> None:
    valid_station = SpaceStation(
        station_id="SS0042",
        name="SpaceStation-0042",
        crew_size=20,
        power_level=100,
        oxygen_level=93.3,
        last_maintenance="2026-09-17",
        is_operational=False,
        notes="We want some fruits"
    )
    print("Space Station Data Validation")
    print("====================================================")
    print(
        "Valid station created:\n"
        f"ID: {valid_station.station_id}\n"
        f"Name: {valid_station.name}\n"
        f"Crew: {valid_station.crew_size}\n"
        f"Power: {valid_station.power_level}%\n"
        f"Oxygen: {valid_station.oxygen_level}%\n"
        f"Last Maintenance: {valid_station.last_maintenance}"
    )
    if valid_station.is_operational:
        print("Status: Operational")
    else:
        print("Status: Operation on hold")
    if valid_station.notes:
        print(f"Notes: {valid_station.notes}\n")
    print("====================================================")
    try:
        invalid_station = SpaceStation(
            station_id="SS0042",
            name="SpaceStation-0042",
            crew_size=20,
            power_level=1000,
            oxygen_level=93.33,
            last_maintenance="65s1d65fw",
            is_operational=True,
            notes="We want some fruits"
        )
        print("No validation error detected")
    except Exception as e:
        print(f"Expected validation error: {e}")


if __name__ == "__main__":

    main()
