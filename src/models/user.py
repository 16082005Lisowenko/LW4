from dataclasses import dataclass, field
from uuid import UUID, uuid4

@dataclass
class User:
    email: str
    role: str
    id: UUID = field(default_factory=uuid4)

    def validate_email(self) -> bool:
        return "@" in self.email

    def is_admin(self) -> bool:
        return self.role == "admin"
