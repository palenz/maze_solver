import unittest
from src.game import Game
from src.make_moves import *


class TestMaze(unittest.TestCase):
    
    def setUp(self):
      self.game = Game("Applejack", 15, 15, 10)
      self.moves = [[15, 'north', 'south'], 'east', [0,'east', 'south'], 'east']

    def test_creates_game(self):
        self.game.create_game()
        self.assertEqual("Applejack", self.game.pony_name)

    def test_get_info(self):
        self.game.create_game()
        self.game.get_info()
        self.assertTrue(self.game.walls)

    def test_calculate_position_east(self):
        result = position_calculator(self.game, 'east', 1)
        self.assertEqual(2, result)

    def test_calculate_position_north(self):
        result = position_calculator(self.game, 'north', 15)
        self.assertEqual(0, result)

    def test_calculate_position_south(self):
        result = position_calculator(self.game, 'south', 0)
        self.assertEqual(15, result)

    def test_calculate_position_west(self):
        result = position_calculator(self.game, 'west', 15)
        self.assertEqual(14, result)

    def test_last_intersection(self):
        expected = [[15, 'north', 'south'], 'east', 'south']
        result = last_intersection(self.moves)
        self.assertEqual(expected, result)

    def test_last_intersection_position(self):
        last = last_intersection_position(self.moves)
        self.assertEqual(0, last)

    def test_south_wall(self):
        result = south_wall(self.game, 224)
        self.assertTrue(result)

    def test_east_wall(self):
        result = east_wall(self.game, 14)
        self.assertTrue(result)

    def test_available_moves(self):
        self.game.create_game()
        result = available_moves(self.game, 20)
        self.assertLessEqual(1, len(result))

    def test_opposite(self):
        opposite_north = 'south'
        self.assertEqual(opposite_north, opposite('north'))

    def test_clean_path(self):
        e = ['north', 'east', 'east', 'east']
        self.assertEqual(e, clean_path(self.moves))

    # The test below will also print the game
    def test_make_move(self):
        self.game.create_game()
        make_move(self.game, "north")
        self.assertTrue(self.game.status_message)

