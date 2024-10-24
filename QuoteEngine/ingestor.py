"""Module to check to choose teh appropriate helper function.

The module usages the technique as described in abstract class
IngestorInterface and call appropriate helper class from
DOCXIngestor, PDFIngestor, TEXTIngestor and CSVIngestor.
"""

from typing import List

from .csv_ingestor import CSVIngestor
from .docx_ingestor import DOCXIngestor
from .ingestor_interface import IngestorInterface
from .pdf_ingestor import PDFIngestor
from .quote_model import QuoteModel
from .text_ingestor import TEXTIngestor


class Ingestor(IngestorInterface):
    """Class Ingestor.

    To select and call the helper class from DOCXIngestor,
    CSVIngestor, PDFIngestor TEXTIngestor
    """

    ingestors = [DOCXIngestor, CSVIngestor, TEXTIngestor, PDFIngestor]

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse correct file from appropriate helper class.

        Parameters:
            path (str) : path of csv csv file location.

        Return:
            List[QuoteModel object] : List of QuoteModel object
        """
        try:
            quote_model_list = []
            for ingestor in cls.ingestors:
                if ingestor.can_ingest(path):
                    quote_model_list.extend(ingestor.parse(path))

            if not quote_model_list:
                raise ValueError(f"No ingestor found for {path}")

            return quote_model_list
        except FileNotFoundError:
            raise FileNotFoundError(f"File not found: {path}")
        except Exception as e:
            raise Exception(f"Error parsing file: {e}")
