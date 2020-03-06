from tic_tac_toe.game_output import GameOutput


def test_game_output_has_an_error_message_for_handling_invalid_user_input(capfd):

    GameOutput().invalid_input_error()

    error_output = capfd.readouterr()

    expected = "\nI'm sorry, I don't understand that.\n"

    assert error_output.out == expected
