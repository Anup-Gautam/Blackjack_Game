from blackjack_helper import *
from test_helper import *
import unittest

class TestBlackjackHelper(unittest.TestCase):
  """
  Class for testing blackjack helper functions.
  """

  def test_print_card_name_example(self):
    """
    Example of a test to compare printed statements with expected

    This does not count as one of your tests
    """
    self.assertEqual(get_print(print_card_name, 2), "Drew a 2\n")

  def test_mock_randint_example(self):
    """
    Example of a test to compare output for a function that calls randint

    This does not count as one of your tests
    """
    self.assertEqual(mock_random([3], draw_card), 3)
    self.assertEqual(mock_random([3, 5], draw_starting_hand, "DEALER"), 8)

  # MAKE SURE ALL YOUR FUNCTION NAMES BEGIN WITH test_
  # WRITE YOUR TESTS BELOW.

  def test_print_card_name(self):
    self.assertEqual(get_print(print_card_name, 2), "Drew a 2\n")
    self.assertEqual(get_print(print_card_name, 1), "Drew an Ace\n")
    self.assertEqual(get_print(print_card_name, 8), "Drew an 8\n")
    self.assertEqual(get_print(print_card_name, 11), "Drew a Jack\n")
    self.assertEqual(get_print(print_card_name, 12), "Drew a Queen\n")
    self.assertEqual(get_print(print_card_name, 13), "Drew a King\n")
    self.assertEqual(get_print(print_card_name, 14), "BAD CARD\n")
    self.assertEqual(get_print(print_card_name, -1), "BAD CARD\n")
    #The code doesn't work at 0. Shows an error.abs

  def test_draw_card(self):
    self.assertEqual(mock_random([2], draw_card), 2)
    self.assertEqual(mock_random([1], draw_card), 11)
    self.assertEqual(mock_random([11], draw_card), 10)
    self.assertEqual(mock_random([12], draw_card), 10)
    self.assertEqual(mock_random([13], draw_card), 10)
    self.assertEqual(mock_random([8], draw_card), 8)
  
  def test_print_header(self):
    self.assertEqual(get_print(print_header, "YOUR TURN"), "-----------\nYOUR TURN\n-----------\n")
    self.assertEqual(get_print(print_header, "DEALER TURN"), "-----------\nDEALER TURN\n-----------\n")
    self.assertEqual(get_print(print_header, "message"), "-----------\nmessage\n-----------\n")

  def test_draw_starting_hand(self):
    self.assertEqual(mock_random([2,6],draw_starting_hand,"YOUR"), 8)
    self.assertEqual(mock_random([2,2],draw_starting_hand,"DEALER"), 4)
    self.assertEqual(mock_random([1,10],draw_starting_hand,"panda"), 21)
    self.assertEqual(mock_random([11,12],draw_starting_hand,"panda"), 20)
  
  def test_print_end_turn_status(self):
    self.assertEqual(get_print(print_end_turn_status,13),"Final hand: 13.\n")
    self.assertEqual(get_print(print_end_turn_status,21),"Final hand: 21.\nBLACKJACK!\n")
    self.assertEqual(get_print(print_end_turn_status,25),"Final hand: 25.\nBUST.\n")

  def test_print_end_game_status(self):
    self.assertEqual(get_print(print_end_game_status, 17, 18),"-----------\nGAME RESULT\n-----------\nDealer wins!\n")
    self.assertEqual(get_print(print_end_game_status, 18, 17),"-----------\nGAME RESULT\n-----------\nYou win!\n")
    self.assertEqual(get_print(print_end_game_status, 18, 18),"-----------\nGAME RESULT\n-----------\nPush.\n")
    self.assertEqual(get_print(print_end_game_status, 18, 21),"-----------\nGAME RESULT\n-----------\nDealer wins!\n")
    self.assertEqual(get_print(print_end_game_status, 21, 18),"-----------\nGAME RESULT\n-----------\nYou win!\n")
    self.assertEqual(get_print(print_end_game_status, 21, 21),"-----------\nGAME RESULT\n-----------\nPush.\n")
    self.assertEqual(get_print(print_end_game_status, 25, 18),"-----------\nGAME RESULT\n-----------\nDealer wins!\n")
    self.assertEqual(get_print(print_end_game_status, 17, 25),"-----------\nGAME RESULT\n-----------\nYou win!\n")
    self.assertEqual(get_print(print_end_game_status, 22, 22),"-----------\nGAME RESULT\n-----------\nDealer wins!\n")
    

    


   

  
  
  








if __name__ == '__main__':
    unittest.main()