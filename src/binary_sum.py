import operator

from src.exceptions import InvalidOperatorError

OPERATOR_SIGNAL_TO_METHOD = {
    '+': operator.add,
    '-': operator.sub,
    '/': operator.truediv,
    '*': operator.mul,
    '%': operator.mod
}


def convert_decimal_numbers_to_binary(decimal_value: float) -> str:
    binary_value = bin(decimal_value).replace('0b', '')
    return '0' * (8 - len(binary_value)) + binary_value


def preform_operation_on_binary_value(
        value_one: str,
        value_two: str,
        calc_operator: str
) -> str:
    if calc_operator not in OPERATOR_SIGNAL_TO_METHOD.keys():
        raise InvalidOperatorError(operator)

    value_one = int(value_one, base=2)
    value_two = int(value_two, base=2)

    operation_result = OPERATOR_SIGNAL_TO_METHOD[calc_operator](
        value_one, value_two
    )

    binary_value = convert_decimal_numbers_to_binary(operation_result)

    return binary_value
