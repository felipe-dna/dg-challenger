from typing import List, Set, Tuple

from src.exceptions import (
    ListOverSizeError,
    InvalidMaximumSizeError,
    MinimumListItemValueError,
    MaximumListItemValueError
)


MINIMUM_PERMITTED_SIZE = -1000
MAXIMUM_PERMITTED_SIZE = 1000


def check_numbers_in_list_size(numbers_list: List[int]) -> None:
    smaller_number = numbers_list[0]
    higher_number = numbers_list[-1]

    if smaller_number < MINIMUM_PERMITTED_SIZE:
        raise MinimumListItemValueError()
    elif higher_number > MAXIMUM_PERMITTED_SIZE:
        raise MaximumListItemValueError()


def get_unique_and_ordered_items(
        max_size: int,
        *numbers: Tuple[int]
) -> List[int]:
    if not 1 <= max_size <= 1000:
        raise InvalidMaximumSizeError()
    elif len(numbers) > max_size:
        raise ListOverSizeError(max_size)

    unique_numbers_set: Set[int] = set(numbers)
    sorted_numbers: List[int] = sorted(unique_numbers_set)

    check_numbers_in_list_size(sorted_numbers)

    return sorted_numbers
