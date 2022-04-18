"""This parses csv files and create quote list."""

import pandas as pd
from typing import List

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel

class CSVIngestor(IngestorInterface):
    """Class to parse csv files and create quote objects."""

    allowed_extensions = ['csv']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse the csv file at the path and return QuoteModel objects."""
        if not cls.can_ingest(path):
            raise Exception("Cannot ingest exceptions")

        quotes = []
        df = pd.read_csv(path, header=0, sep=',', error_bad_lines=False)
        for _, row in df.iterrows():
            quote = QuoteModel(row['body'], row['author'])
            quotes.append(quote)

        return quotes