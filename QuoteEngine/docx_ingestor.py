"""Module to ingest 'docx' type file.

The module usages the technique as described in abstract class
IngestorInterface.
"""

from typing import List

import docx

from .ingestor_interface import IngestorInterface
from .quote_model import QuoteModel


class DOCXIngestor(IngestorInterface):
    """Class DOCXIngestor.

    The class manipulate the 'docx' type file, parse the quote and auther
    and retrun the QuoteModel object list.
    """

    allowed_file_extention: List[str] = ["docx"]

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse 'docx' file.

        The classmethod 'parse()' extract the 'quote' and Author
        returns the list of QuoteModel.
        Parameters:
            path (str) : path of 'docx' file location.

        Return:
            List[QuoteModel object] : List of QuoteModel object
        """
        try:
            if cls.can_ingest(path):
                quote_list: List[QuoteModel] = []
                doc_file = docx.Document(path)

                for doc_para in iter(doc_file.paragraphs):
                    txt = doc_para.text.split("-")
                    if len(txt) < 2:
                        continue
                    quote_list.append(
                        QuoteModel(
                            txt[0].strip("\n\r").strip(),
                            txt[1].strip("\n\r").strip()
                        )
                    )

                return quote_list
            else:
                raise ValueError(
                    f"Unable to parse {path}." +
                    "Allowed file types: pdf,docx,csv,txt."
                )
        except FileNotFoundError:
            raise FileNotFoundError(f"File not found: {path}")
        except Exception as e:
            raise Exception(f"Error parsing 'docx' file: {e}")
