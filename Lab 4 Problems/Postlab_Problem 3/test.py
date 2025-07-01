import unittest
from unittest.mock import patch, mock_open
import oxo_logic

class TestOxoLogic(unittest.TestCase):

    def test_new_game_is_empty(self):
        game = oxo_logic.newGame()
        self.assertEqual(len(game), 9)
        self.assertTrue(all(cell == ' ' for cell in game))

    def test_user_move_valid(self):
        game = oxo_logic.newGame()
        result = oxo_logic.userMove(game, 0)
        self.assertEqual(game[0], 'X')
        self.assertEqual(result, '')

    def test_user_move_invalid(self):
        game = oxo_logic.newGame()
        game[0] = 'X'
        with self.assertRaises(ValueError):
            oxo_logic.userMove(game, 0)

    def test_computer_move_returns_O_or_D_or_blank(self):
        game = oxo_logic.newGame()
        result = oxo_logic.computerMove(game)
        self.assertIn(result, ('O', 'D', ''))

    def test_user_win(self):
        game = ['X', 'X', ' ',  # Simulate board with 2 X's in a row
                ' ', ' ', ' ',
                ' ', ' ', ' ']
        result = oxo_logic.userMove(game, 2)
        self.assertEqual(result, 'X')

    def test_computer_win(self):
        game = ['O', 'O', ' ',  # Simulate board with 2 O's in a row
                ' ', ' ', ' ',
                ' ', ' ', ' ']
        # Force _generateMove to pick index 2
        with patch('oxo_logic._generateMove', return_value=2):
            result = oxo_logic.computerMove(game)
        self.assertEqual(result, 'O')

    def test_draw(self):
        game = ['X', 'O', 'X',
                'X', 'O', 'O',
                'O', 'X', ' ']  # Only one move left
        with patch('oxo_logic._generateMove', return_value=8):
            result = oxo_logic.computerMove(game)
        self.assertEqual(result, 'D')

    @patch('oxo_data.saveGame')
    def test_save_game_called(self, mock_save):
        game = oxo_logic.newGame()
        oxo_logic.saveGame(game)
        mock_save.assert_called_once_with(game)

    @patch('oxo_data.restoreGame', return_value=list("XO XO XO "))
    def test_restore_game_valid(self, mock_restore):
        game = oxo_logic.restoreGame()
        self.assertEqual(game, list("XO XO XO "))

    @patch('oxo_data.restoreGame', return_value=list("X" * 5))  # invalid length
    def test_restore_game_invalid_length(self, mock_restore):
        game = oxo_logic.restoreGame()
        self.assertEqual(game, [' '] * 9)

    @patch('oxo_data.restoreGame', side_effect=IOError("File not found"))
    def test_restore_game_ioerror(self, mock_restore):
        game = oxo_logic.restoreGame()
        self.assertEqual(game, [' '] * 9)

if __name__ == '__main__':
    unittest.main()
