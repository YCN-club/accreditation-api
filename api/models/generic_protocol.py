from typing import Protocol


class GenericProtocol(Protocol):
    def to_dict(self) -> dict:
        """Convert the object to a dictionary"""
