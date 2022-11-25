from unittest import TestCase, main
from unittest.mock import patch
from test_helper import run_test

class TestBlackjack(TestCase):

    @patch('blackjack_helper.randint')
    @patch('builtins.input')
    def test_example(self, input_mock, randint_mock):
        '''
        Both the dealer and user receive cards that end up with a hand less than 21.
        The dealer wins by having a higher hand than the user.

        This does not count as one of your tests.
        '''
        output = run_test([3, 5, 8], ['y', 'n'], [3, 5, 10], randint_mock, input_mock)
        expected = "-----------\n" \
                   "YOUR TURN\n" \
                   "-----------\n" \
                   "Drew a 3\n" \
                   "Drew a 5\n" \
                   "You have 8. Hit (y/n)? y\n" \
                   "Drew an 8\n" \
                   "You have 16. Hit (y/n)? n\n" \
                   "Final hand: 16.\n" \
                   "-----------\n" \
                   "DEALER TURN\n" \
                   "-----------\n" \
                   "Drew a 3\n" \
                   "Drew a 5\n" \
                   "Dealer has 8.\n" \
                   "Drew a 10\n" \
                   "Final hand: 18.\n" \
                   "-----------\n" \
                   "GAME RESULT\n" \
                   "-----------\n" \
                   "Dealer wins!\n"
        self.assertEqual(output, expected)

    # Make sure all your test functions start with test_ 
    # Follow indentation of test_example
    # WRITE ALL YOUR TESTS BELOW. Do not delete this line.
        
        #test1: Normal TestCase , 8, King test
    @patch('blackjack_helper.randint')
    @patch('builtins.input')
    def test_normal(self, input_mock, randint_mock):
        output = run_test([3, 5, 8], ['y', 'n'], [3, 5, 13], randint_mock, input_mock)
        expected = "-----------\n" \
                   "YOUR TURN\n" \
                   "-----------\n" \
                   "Drew a 3\n" \
                   "Drew a 5\n" \
                   "You have 8. Hit (y/n)? y\n" \
                   "Drew an 8\n" \
                   "You have 16. Hit (y/n)? n\n" \
                   "Final hand: 16.\n" \
                   "-----------\n" \
                   "DEALER TURN\n" \
                   "-----------\n" \
                   "Drew a 3\n" \
                   "Drew a 5\n" \
                   "Dealer has 8.\n" \
                   "Drew a King\n" \
                   "Final hand: 18.\n" \
                   "-----------\n" \
                   "GAME RESULT\n" \
                   "-----------\n" \
                   "Dealer wins!\n"
        self.assertEqual(output, expected)

        #test 2: Dealer Bust, Player Bust tescase, Dealer wins
    @patch('blackjack_helper.randint')
    @patch('builtins.input')
    def test_dealer_bust_player_bust(self, input_mock, randint_mock):
        output = run_test([3, 1, 13], ['y'], [2, 13, 10], randint_mock, input_mock)
        expected = "-----------\n" \
                   "YOUR TURN\n" \
                   "-----------\n" \
                   "Drew a 3\n" \
                   "Drew an Ace\n" \
                   "You have 14. Hit (y/n)? y\n" \
                   "Drew a King\n" \
                   "Final hand: 24.\n" \
                   "BUST.\n" \
                   "-----------\n" \
                   "DEALER TURN\n" \
                   "-----------\n" \
                   "Drew a 2\n" \
                   "Drew a King\n" \
                   "Dealer has 12.\n" \
                   "Drew a 10\n" \
                   "Final hand: 22.\n" \
                   "BUST.\n" \
                   "-----------\n" \
                   "GAME RESULT\n" \
                   "-----------\n" \
                   "Dealer wins!\n"
        self.assertEqual(output, expected)

         #test 3: Dealer normal, Player Bust tescase, Dealer wins
    @patch('blackjack_helper.randint')
    @patch('builtins.input')
    def test_dealer_normal_player_bust(self, input_mock, randint_mock):
        output = run_test([3, 1, 13], ['y'], [2, 13, 5], randint_mock, input_mock)
        expected = "-----------\n" \
                   "YOUR TURN\n" \
                   "-----------\n" \
                   "Drew a 3\n" \
                   "Drew an Ace\n" \
                   "You have 14. Hit (y/n)? y\n" \
                   "Drew a King\n" \
                   "Final hand: 24.\n" \
                   "BUST.\n" \
                   "-----------\n" \
                   "DEALER TURN\n" \
                   "-----------\n" \
                   "Drew a 2\n" \
                   "Drew a King\n" \
                   "Dealer has 12.\n" \
                   "Drew a 5\n" \
                   "Final hand: 17.\n" \
                   "-----------\n" \
                   "GAME RESULT\n" \
                   "-----------\n" \
                   "Dealer wins!\n"
        self.assertEqual(output, expected)

        #test 4: dealer_bust, player_normal, player wins
    @patch('blackjack_helper.randint')
    @patch('builtins.input')
    def test_dealer_bust_player_normal(self, input_mock, randint_mock):
        output = run_test([3, 5, 13], ['y','n'], [2, 13, 1], randint_mock, input_mock)
        expected = "-----------\n" \
                   "YOUR TURN\n" \
                   "-----------\n" \
                   "Drew a 3\n" \
                   "Drew a 5\n" \
                   "You have 8. Hit (y/n)? y\n" \
                   "Drew a King\n" \
                   "You have 18. Hit (y/n)? n\n" \
                   "Final hand: 18.\n" \
                   "-----------\n" \
                   "DEALER TURN\n" \
                   "-----------\n" \
                   "Drew a 2\n" \
                   "Drew a King\n" \
                   "Dealer has 12.\n" \
                   "Drew an Ace\n" \
                   "Final hand: 23.\n" \
                   "BUST.\n" \
                   "-----------\n" \
                   "GAME RESULT\n" \
                   "-----------\n" \
                   "You win!\n"
        self.assertEqual(output, expected)

        #test 5: dealer normal player blackjack
    @patch('blackjack_helper.randint')
    @patch('builtins.input')
    def test_dealer_normal_player_bj(self, input_mock, randint_mock):
        output = run_test([3, 1, 7], ['x','y'], [2, 13, 5], randint_mock, input_mock)
        expected = "-----------\n" \
                   "YOUR TURN\n" \
                   "-----------\n" \
                   "Drew a 3\n" \
                   "Drew an Ace\n" \
                   "You have 14. Hit (y/n)? x\n" \
                   "Sorry I didn't get that.\n" \
                   "You have 14. Hit (y/n)? y\n" \
                   "Drew a 7\n" \
                   "Final hand: 21.\n" \
                   "BLACKJACK!\n" \
                   "-----------\n" \
                   "DEALER TURN\n" \
                   "-----------\n" \
                   "Drew a 2\n" \
                   "Drew a King\n" \
                   "Dealer has 12.\n" \
                   "Drew a 5\n" \
                   "Final hand: 17.\n" \
                   "-----------\n" \
                   "GAME RESULT\n" \
                   "-----------\n" \
                   "You win!\n"
        self.assertEqual(output, expected)
        
        #test 6; normal:player, Blackjack:dealer , Ace, 2, Jack, Queen test

    @patch('blackjack_helper.randint')
    @patch('builtins.input')
    def test_player_dealer_bj(self, input_mock, randint_mock):
        output = run_test([2, 11, 7 ], ['y', 'n'], [1, 12], randint_mock, input_mock)
        expected = "-----------\n" \
                   "YOUR TURN\n" \
                   "-----------\n" \
                   "Drew a 2\n" \
                   "Drew a Jack\n" \
                   "You have 12. Hit (y/n)? y\n" \
                   "Drew a 7\n" \
                   "You have 19. Hit (y/n)? n\n" \
                   "Final hand: 19.\n" \
                   "-----------\n" \
                   "DEALER TURN\n" \
                   "-----------\n" \
                   "Drew an Ace\n" \
                   "Drew a Queen\n" \
                   "Final hand: 21.\n" \
                   "BLACKJACK!\n" \
                   "-----------\n" \
                   "GAME RESULT\n" \
                   "-----------\n" \
                   "Dealer wins!\n"
        self.assertEqual(output, expected)


        #test 7: Dealer > Player test
    @patch('blackjack_helper.randint')
    @patch('builtins.input')
    def test_dealer_greater(self, input_mock, randint_mock):
        output = run_test([2, 11, 7 ], ['y', 'n'], [10, 12], randint_mock, input_mock)
        expected = "-----------\n" \
                   "YOUR TURN\n" \
                   "-----------\n" \
                   "Drew a 2\n" \
                   "Drew a Jack\n" \
                   "You have 12. Hit (y/n)? y\n" \
                   "Drew a 7\n" \
                   "You have 19. Hit (y/n)? n\n" \
                   "Final hand: 19.\n" \
                   "-----------\n" \
                   "DEALER TURN\n" \
                   "-----------\n" \
                   "Drew a 10\n" \
                   "Drew a Queen\n" \
                   "Final hand: 20.\n" \
                   "-----------\n" \
                   "GAME RESULT\n" \
                   "-----------\n" \
                   "Dealer wins!\n"
        self.assertEqual(output, expected)

        #test 8: Player BJ = Dealer test BJ
    @patch('blackjack_helper.randint')
    @patch('builtins.input')
    def test_dealer_player_bjequal(self, input_mock, randint_mock):
        output = run_test([3, 11, 8 ], ['y'], [10, 1], randint_mock, input_mock)
        expected = "-----------\n" \
                   "YOUR TURN\n" \
                   "-----------\n" \
                   "Drew a 3\n" \
                   "Drew a Jack\n" \
                   "You have 13. Hit (y/n)? y\n" \
                   "Drew an 8\n" \
                   "Final hand: 21.\n" \
                   "BLACKJACK!\n" \
                   "-----------\n" \
                   "DEALER TURN\n" \
                   "-----------\n" \
                   "Drew a 10\n" \
                   "Drew an Ace\n" \
                   "Final hand: 21.\n" \
                   "BLACKJACK!\n" \
                   "-----------\n" \
                   "GAME RESULT\n" \
                   "-----------\n" \
                   "Push.\n"
        self.assertEqual(output, expected)

        #test 9: Player > Dealer
    @patch('blackjack_helper.randint')
    @patch('builtins.input')
    def test_player_greater(self, input_mock, randint_mock):
        output = run_test([2, 11, 7 ], ['y', 'n'], [10, 8], randint_mock, input_mock)
        expected = "-----------\n" \
                   "YOUR TURN\n" \
                   "-----------\n" \
                   "Drew a 2\n" \
                   "Drew a Jack\n" \
                   "You have 12. Hit (y/n)? y\n" \
                   "Drew a 7\n" \
                   "You have 19. Hit (y/n)? n\n" \
                   "Final hand: 19.\n" \
                   "-----------\n" \
                   "DEALER TURN\n" \
                   "-----------\n" \
                   "Drew a 10\n" \
                   "Drew an 8\n" \
                   "Final hand: 18.\n" \
                   "-----------\n" \
                   "GAME RESULT\n" \
                   "-----------\n" \
                   "You win!\n"
        self.assertEqual(output, expected)

    #test 10: Player nomral = Dealer normal
    @patch('blackjack_helper.randint')
    @patch('builtins.input')
    def test_dealer_player_equal(self, input_mock, randint_mock):
        output = run_test([3, 5, 8, 2 ], ['y', 'y','n'], [13, 8], randint_mock, input_mock)
        expected = "-----------\n" \
                   "YOUR TURN\n" \
                   "-----------\n" \
                   "Drew a 3\n" \
                   "Drew a 5\n" \
                   "You have 8. Hit (y/n)? y\n" \
                   "Drew an 8\n" \
                   "You have 16. Hit (y/n)? y\n" \
                   "Drew a 2\n" \
                   "You have 18. Hit (y/n)? n\n" \
                   "Final hand: 18.\n" \
                   "-----------\n" \
                   "DEALER TURN\n" \
                   "-----------\n" \
                   "Drew a King\n" \
                   "Drew an 8\n" \
                   "Final hand: 18.\n" \
                   "-----------\n" \
                   "GAME RESULT\n" \
                   "-----------\n" \
                   "Push.\n"
        self.assertEqual(output, expected) 

        

    # Write all your tests above this. Do not delete this line.

if __name__ == '__main__':
    main()