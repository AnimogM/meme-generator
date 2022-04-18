"""This creates new quote."""

class QuoteModel():
    """Creates a new quote."""

    def __init__(self, body, author):
        """Initializes quote."""
        self.body = body
        self.author = author

    def __repr__(self):
        """Return {quote body text} - {author}."""
        return f"{self.body} - {self.author}"