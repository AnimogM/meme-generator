"""This parses pdf files and create quote objects."""

import subprocess
import random
import os
from typing import List

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class PDFIngestor(IngestorInterface):
    """Class to parse pdf files and create quote objects."""

    allowed_extensions = ['pdf']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse the file at the given path and return QuoteModel objects."""
        quotes = []
        if not cls.can_ingest(path):
            raise Exception("Cannot ingest exception")

        temp = f'./tmp/{random.randint(0, 10000)}.txt'
        try:
            call = subprocess.call(['pdftotext', path, temp])
            with open(temp, 'r') as f:
                file_lines_content = f.readlines()
        except FileNotFoundError as filenotfounderror:
            print(f'Error: {filenotfounderror}')
            return quotes

        for line in file_lines_content:
            line = line.strip('\n\r').strip()
            line_length = len(line)
            if line_length > 0:
                parsed_line = line.split(' - ')
                quote_modell = QuoteModel(parsed_line[0], parsed_line[1])
                quotes.append(quote_modell)

        f.close()
        os.remove(temp)
        return quotes