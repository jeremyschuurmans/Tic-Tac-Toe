from unittest import mock
import pytest

from tic_tac_toe.player import Player
from tic_tac_toe.errors import InputNotNumericError


@mock.patch("tic_tac_toe.player.input")
def test_user_input_raises_input_not_numeric_error(mocked_input):
    mocked_input.return_value = "a"

    with pytest.raises(InputNotNumericError):
        Player(token=["X"]).get_input()
