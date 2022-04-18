"""This is a base class for parsing files and create quote objects."""

from abc import ABC, abstractmethod
from typing import List

from .QuoteModel import QuoteModel


class IngestorInterface(ABC):
    """Base class for parsing files and create quote objects."""

    allowed_extensions = []

    @classmethod
    def can_ingest(cls, path: str) -> bool:
        """Check if file can be parsed."""
        exn = path.split('.')[-1]
        return exn in cls.allowed_extensions

    @classmethod
    @abstractmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Abstract method to parse the allowed file and return QuoteModel objects."""
        pass