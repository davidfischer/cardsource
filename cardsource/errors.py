class CardSourceError(Exception):
    pass


class InvalidRankError(CardSourceError):
    pass


class InvalidSuitError(CardSourceError):
    pass
