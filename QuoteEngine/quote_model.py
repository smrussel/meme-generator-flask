"""Module for encapsulating Quote body and Author."""


class QuoteModel:
    """Class for collect the Quote body and Author.

    Arguments:
        body (str) -> Quote body.
        author (str) -> Name of Author of the citation

    Return:
        QuoteModel object.

    Usages:
        QuoteModel(body, author) -> Instantiate QuoteModel object
    or,
        QuoteModel.quote_parser(body, author) ->
                            Instantiate QuoteModel Object
    """

    def __init__(self, body: str, author: str) -> None:
        """Parameters: body(str), author(str).

        Return: its own instantiated object
        """
        self.body = body
        self.author = author

    @classmethod
    def quote_parser(cls, body: str, author: str) -> object:
        """parameter: body(str), author(str).

        Return: instantiated QuoteModel object
        """
        return cls(body, author)

    def __str__(self):
        """Return a string representation of the quote.

        This method formats the quote as a string and returns it.
        """
        return f"Quote : {self.body}, Author : {self.author}"
