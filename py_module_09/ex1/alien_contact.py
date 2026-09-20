from pydantic import BaseModel, model_validator, Field, ValidationError
from datetime import datetime
from typing import Optional
from enum import Enum


class ContactType(Enum):
    RADIO = "radio"
    VISUAL = "visual"
    PHYSICAL = "physical"
    TELEPATIC = "telepatic"


class AlienContact(BaseModel):
    contact_id: str = Field(..., min_length=5, max_length=15)
    timestamp: datetime
    location: str = Field(..., min_length=3, max_length=100)
    contact_type: ContactType = Field(...)
    signal_strength: float = Field(..., ge=0.0, le=10.0)
    duration_minutes: int = Field(..., ge=1, le=1440)
    witness_count: int = Field(..., ge=1, le=100)
    message_received: Optional[str] = Field(default=None, max_length=500)
    is_verified: bool = Field(default=False)

    @model_validator(mode='after')
    def business_rules(self) -> 'AlienContact':
        errors = []
        if self.contact_id[:2] != "AC":
            errors.append("contact_id should start with 'AC'.")
        if self.contact_type == ContactType.PHYSICAL and not self.is_verified:
            errors.append("Can not verify the physical contact.")
        if ((self.contact_type == ContactType.TELEPATIC) and
           (self.witness_count < 3)):
            errors.append("Not enough witness to verify Telepathic contact. "
                          "Requires minimum 3 witnesses.")
        if self.signal_strength >= 7.0 and not self.message_received:
            errors.append("Signal strength is strong. Check message.")
        if errors:
            raise ValueError("; ".join(errors))
        print(errors)
        return self


def main() -> None:
    contact_a = AlienContact(
                    contact_id="AC-123",
                    timestamp=datetime.today(),
                    location="Area 42, Amsterdam, NL",
                    contact_type=ContactType.TELEPATIC.value,
                    signal_strength=4.42,
                    duration_minutes=3,
                    witness_count=4,
                    message_received="asdfadfasdf",
                    is_verified=True
                    )
    print("Alien Contact Log validation")
    print("============================")
    print("Valid Contact Report:")
    print(f"ID: {contact_a.contact_id}")
    print(f"Type: {contact_a.contact_type.value}")
    print(f"Location: {contact_a.location}")
    print(f"Signal: {contact_a.signal_strength}/10")
    print(f"Duration: {contact_a.duration_minutes} minutes")
    print(f"Witnesses: {contact_a.witness_count}")
    if contact_a.message_received:
        print(f"Message: {contact_a.message_received}")
    if contact_a.is_verified:
        print("Verification: Verified")
    else:
        print("Verification: Not verified")
    print()
    print("============================")
    print("Expected validation error(s):")
    try:
        AlienContact(
                    contact_id="AC-123",
                    timestamp=datetime.today(),
                    location="Area 42, Amsterdam, NL",
                    contact_type=ContactType.TELEPATIC.value,
                    signal_strength=7.42,
                    duration_minutes=3,
                    witness_count=2,
                    message_received=None,
                    is_verified=False
                    )
    except ValidationError as e:
        for err in e.errors():
            print(f" {err['msg']}")


if __name__ == "__main__":
    main()
