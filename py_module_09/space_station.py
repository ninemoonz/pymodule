from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field
# Field, model_validator


class SpaceStation(BaseModel):
    station_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=1, max_length=50)
    crew_size: int = Field(ge=1, le=20)
    power_level: float = Field(multiple_of=0.1, ge=0.0, le=100.0)
    oxygen_level: float = Field(multiple_of=0.1, ge=0.0, le=100.0)
    last_maintenance: datetime
    is_operational: bool = Field(default=True)
    notes: Optional[str] = Field(default=None, max_length=200)


def main(station: SpaceStation) -> None:
    print("Space Station Data Validation")
    print("====================================================")
    print(
        "Valid station created:\n"
        f"ID: {station.station_id}\n"
        f"Name: {station.name}\n"
        f"Crew: {station.crew_size}\n"
        f"Power: {station.power_level}%\n"
        f"Oxygen: {station.oxygen_level}%\n"
        f"Last Maintenance: {station.last_maintenance}\n"
    )
    if station.is_operational:
        print("Status: Operational")
    else:
        print("Status: Operation on hold")
    if station.notes:
        print(f"Notes: {station.notes}\n")
    print("====================================================")
    print("Expected validation error:")


if __name__ == "__main__":
    station_a = SpaceStation(
        station_id="SS0042",
        name="SpaceStation-0042",
        crew_size=12,
        power_level=100,
        oxygen_level=93.3,
        last_maintenance="2026-09-17",
        is_operational=True,
        notes="Ready to activate"
    )
    main(station_a)
