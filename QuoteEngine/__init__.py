"""Package for extracting quotes from a variety of file types."""

from .pdf_ingestor import PDFIngestor
from .text_ingestor import TEXTIngestor
from .csv_ingestor import CSVIngestor
from .docx_ingestor import DOCXIngestor
from .quote_model import QuoteModel
from .ingestor import Ingestor
