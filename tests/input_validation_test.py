from unittest import mock
import pytest

from tic_tac_toe.user_input import UserInput
from tic_tac_toe.board import Board
from tic_tac_toe.errors import InputNotNumericError


@mock.patch("tic_tac_toe.user_input.input")
def test_user_input_raises_input_not_numeric_error(mocked_input):
    mocked_input.return_value = "a"

    with pytest.raises(InputNotNumericError):
        UserInput().process_input()
