from pydantic import BaseModel, model_validator, Field, ValidationError
from datetime import datetime
from typing import Optional
from enum import Enum


class ContactType(Enum):
    RADIO = "radio"
    VISUAL = "visual"
    PHYSICAL = "physical"
    TELEPHATIC = "telephatic"


class AlienContact(BaseModel):
    contact_id: str = Field(..., min_length=5, max_length=15)
    timestamp: datetime
    location: str = Field(..., min_length=3, max_length=100)
    contact_type: ContactType = Field(...)
    signal_strength: float = Field(..., ge=0.0, le=10.0)
    duration_minutes: int = Field(..., ge=1, le=1440)
    witness_count: int = Field(..., ge=1, le=100)
    message_received: Optional[str] = Field(max_length=500)
    is_verified: bool = Field(default=False)


def main() -> None:
    contact_a = AlienContact(
                    contact_id="AC-123",
                    timestamp=datetime.today(),
                    location="Area 42, Amsterdam, NL",
                    contact_type=ContactType.PHYSICAL.value,
                    signal_strength=4.42,
                    duration_minutes=3,
                    witness_count=7,
                    message_received="asdfadfasdf",
                    is_verified=True
                    )
    print("Alien Contact Log validation")
    print("============================")
    print("Valid Contact Report:")
    print(f"ID: {contact_a.contact_id}")
    print(f"Type: {contact_a.contact_type}")
    print(f"Location: {contact_a.location}")
    print(f"Signal: {contact_a.signal_strength}/10")
    print(f"Duration: {contact_a.duration_minutes} minutes")
    print(f"Witnesses: {contact_a.witness_count}")
    if contact_a.message_received:
        print(f"Message: {contact_a.message_received}")
    print()
    print("============================")
    print("Expected validation error(s):")
    try:
        AlienContact(
                    contact_id="AC-123",
                    timestamp=datetime.today(),
                    location="Area 42, Amsterdam, NL",
                    contact_type=ContactType.PHYSICAL.value,
                    signal_strength=4.42,
                    duration_minutes=3,
                    witness_count=7,
                    message_received="asdfadfasdf",
                    is_verified=True
                    )
    except ValidationError as e:
        for err in e.errors():
            print(f" {'.'.join(str(x) for x in err['loc'])}: {err['msg']}")


if __name__ == "__main__":
    main()
