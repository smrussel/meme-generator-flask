"""Module to ingest csv type file.

The module usages the technique as described in abstract class
IngestorInterface.
"""

from typing import List

import pandas

from .ingestor_interface import IngestorInterface
from .quote_model import QuoteModel


class CSVIngestor(IngestorInterface):
    """Class CSVIngestor.

    The class manipulate the csv type file, parse the quote and auther
    and retrun the QuoteModel object list.
    """

    allowed_file_extention: List[str] = ["csv"]

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse CSV file.

        The classmethod 'parse()' extract the 'quote' and Author
        return the list of QuoteModel.
        Parameters:
            path (str) : path of csv csv file location.

        Return:
            List[QuoteModel object] : List of QuoteModel object
        """
        try:
            if cls.can_ingest(path):
                quote_list: List[QuoteModel] = []
                df = pandas.read_csv(path)
                for index, row in df.iterrows():
                    quote = QuoteModel(row["body"], row["author"])
                    quote_list.append(quote)
                return quote_list
            else:
                raise ValueError(
                    f"Unable to parse {path}." +
                    "Allowed file types: pdf,docx,csv,txt."
                )
        except FileNotFoundError:
            raise FileNotFoundError(f"File not found: {path}")
        except pandas.errors.EmptyDataError:
            raise ValueError(f"File is empty: {path}")
        except KeyError as e:
            raise KeyError(f"Required columns not found in CSV: {e}")
        except Exception as e:
            raise Exception(f"Error parsing CSV: {e}")
