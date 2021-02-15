import pytest

from src.exceptions import (
    ListOverSizeError,
    InvalidMaximumSizeError,
    MaximumListItemValueError,
    MinimumListItemValueError
)

from src.question_01 import (
    get_unique_and_ordered_items,
    MAXIMUM_PERMITTED_SIZE,
    MINIMUM_PERMITTED_SIZE
)


FIRST_ENTRY = [10, 10, 9, 9, 8, 8, 7, 7, 6, 6]
SECOND_ENTRY = [5, -1, -1, -1, -1, -1]
THIRD_ENTRY = [5, -123, 123, 999, 1000, -1000]


def test_send_an_list_of_numbers_with_size_higher_than_the_allowed() -> None:
    max_size = 3
    elements_list = [1, 2, 3, 4]

    with pytest.raises(ListOverSizeError):
        get_unique_and_ordered_items(max_size, *elements_list)


def test_send_an_max_size_higher_than_the_allowed() -> None:
    max_size = 1001
    elements_list = [1, 2, 3]

    with pytest.raises(InvalidMaximumSizeError):
        get_unique_and_ordered_items(max_size, *elements_list)


def test_send_an_max_size_smaller_than_the_allowed() -> None:
    max_size = 0
    elements_list = [1, 2, 3]

    with pytest.raises(InvalidMaximumSizeError):
        get_unique_and_ordered_items(max_size, *elements_list)


def test_send_an_list_number_higher_than_the_allowed() -> None:
    max_size = 10
    elements_list = [1, 2, 3, (MAXIMUM_PERMITTED_SIZE + 1)]

    with pytest.raises(MaximumListItemValueError):
        get_unique_and_ordered_items(max_size, *elements_list)


def test_send_an_list_number_smaller_than_the_allowed() -> None:
    max_size = 3
    elements_list = [1, 2, (MINIMUM_PERMITTED_SIZE - 1)]

    with pytest.raises(MinimumListItemValueError):
        get_unique_and_ordered_items(max_size, *elements_list)


def test_the_first_entry_must_contains_ordered_numbers() -> None:
    result = get_unique_and_ordered_items(*FIRST_ENTRY)

    current_max_number = -1001
    for number in result:
        assert number > current_max_number
        current_max_number = number


def test_the_second_entry_must_contains_ordered_numbers() -> None:
    result = get_unique_and_ordered_items(*SECOND_ENTRY)

    current_max_number = -1001
    for number in result:
        assert number > current_max_number
        current_max_number = number


def test_the_third_entry_must_contains_ordered_numbers() -> None:
    result = get_unique_and_ordered_items(*THIRD_ENTRY)

    current_max_number = -1001
    for number in result:
        assert number > current_max_number
        current_max_number = number


def test_the_first_entry_must_contain_just_unique_numbers() -> None:
    result = get_unique_and_ordered_items(*FIRST_ENTRY)

    result_copy_list = result
    for index, item in enumerate(result):
        result_copy_list.pop(index)
        assert item not in result_copy_list


def test_the_second_entry_must_contain_just_unique_numbers() -> None:
    result = get_unique_and_ordered_items(*SECOND_ENTRY)

    result_copy_list = result
    for index, item in enumerate(result):
        result_copy_list.pop(index)
        assert item not in result_copy_list


def test_the_third_entry_must_contain_just_unique_numbers() -> None:
    result = get_unique_and_ordered_items(*THIRD_ENTRY)

    result_copy_list = result
    for index, item in enumerate(result):
        result_copy_list.pop(index)
        assert item not in result_copy_list
