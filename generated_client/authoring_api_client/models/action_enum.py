from enum import Enum


class ActionEnum(str, Enum):
    ALLOW = "allow"
    REVOKE = "revoke"

    def __str__(self) -> str:
        return str(self.value)
