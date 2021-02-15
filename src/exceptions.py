class ListOverSizeError(Exception):
    def __init__(self, size: int) -> None:
        self.message = f'Invalid number of items in the array. The maximum is' \
                       f' {size}.'


class InvalidMaximumSizeError(Exception):
    def __init__(self) -> None:
        self.message = f'The `max_size` parameters must be >= 1 and <= 1000.'


class MinimumListItemValueError(Exception):
    def __init__(self) -> None:
        self.message = 'The numbers list you sent contains numbers smaller ' \
                       'than allowed.'


class MaximumListItemValueError(Exception):
    def __init__(self) -> None:
        self.message = 'The numbers list you sent contains numbers larger ' \
                       'than allowed.'
