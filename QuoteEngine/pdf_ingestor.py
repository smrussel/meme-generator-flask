"""Module to ingest pdf type file.

The module usages the technique as described in abstract class
IngestorInterface.
"""

import os
import random
import subprocess
from typing import List

from .ingestor_interface import IngestorInterface
from .quote_model import QuoteModel


class PDFIngestor(IngestorInterface):
    """Class PDFIngestor.

    The class manipulate the pdf type file, parse the quote and auther
     and retrun the QuoteModel object list.

    """

    allowed_file_extention: List[str] = ["pdf"]

    @staticmethod
    def pdftotxt(path: str) -> str:
        """Convert pdf to txt file.

        parameters:
            path (str): path of pdf.
        return:
            path (str) : path of created txt file.
        """
        txt_file = f"./{random.randint(0, 10000000)}.txt"

        try:
            subprocess.Popen(["touch", txt_file])
            subprocess.call(["pdftotext", path, txt_file],
                            stderr=subprocess.STDOUT)
            return txt_file
        except Exception as e:
            if os.path.exists(txt_file):
                os.remove(txt_file)
            raise e

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse txt file.

        The classmethod 'parse()' extract the 'quote' and Author
        returns the list of QuoteModel.
        Parameters:
            path (str) : path of 'txt' file location.

        Return:
            List[QuoteModel object] : List of QuoteModel object
        """
        try:
            if cls.can_ingest(path):
                path = cls.pdftotxt(path)
                quote_list: List[QuoteModel] = []
                with open(path, "r") as txt_obj:
                    lines = txt_obj.readlines()
                    for line in iter(lines):
                        line = line.strip("\n\n").strip()
                        if len(line) < 3:
                            continue
                        quote, author = tuple(line.split(" - "))
                        quote_list.append(QuoteModel(quote, author))
                os.remove(path)
                return quote_list
            else:
                raise ValueError(
                    f"Unable to parse {path}." +
                    "Allowed file types: pdf,docx,csv,txt."
                )
        except FileNotFoundError:
            raise FileNotFoundError(f"File not found: {path}")
        except Exception as e:
            raise Exception(f"Error parsing PDF file: {e}")
