"""This parses docx files and create quote objects."""

import docx
from typing import List

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class DocxIngestor(IngestorInterface):
    """Class to parse docx files and create quote objects."""

    allowed_extensions = ['docx']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse the file at the given path and return QuoteModel objects."""
        if not cls.can_ingest(path):
            raise Exception("Cannot ingest exceptions")

        docx_file = docx.Document(path)
        quotes = []
        for para in docx_file.paragraphs:
            if para.text != "":
                parsed_text = para.text.split(' - ')
                quote_model = QuoteModel(parsed_text[0], parsed_text[1])
                quotes.append(quote_model)

        return quotes