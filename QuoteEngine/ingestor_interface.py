"""Module IngestorInterface.

Module encapsulates IngestorInterface class with all the generic
'abstractmethods' and 'classmethods'.
"""

from abc import ABC, abstractmethod
from typing import List

from .quote_model import QuoteModel


class IngestorInterface(ABC):
    """Abstractclass IngestoInterface."""

    allowed_file_extention: List[str] = []

    @classmethod
    @abstractmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse function should be implemented at the stratgy class."""
        pass

    @classmethod
    def can_ingest(cls, path: str) -> bool:
        """Can_ingest classmethod will check for correct file extension."""
        extention = path.split(".")[-1]
        return extention in cls.allowed_file_extention
