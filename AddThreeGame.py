# Author: Matthew Armstrong
# Date: 08/05/2021
# Description: A game where two players can select 3 integers ranging from 1-9,
# and the numbers sum to 15. One day I will fix this code.
class AddThreeGame:
    """Represents an Add Three Game, where two players can select 3 integers ranging from 1-9,
    and the numbers sum to 15"""
    def __init__(self):
        """Private classes for the Add Three Game"""
        self._first_list = []
        self._second_list = []
        self._input_number = []
        self._valid_choices = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self._current_state = "UNFINISHED"

    def get_current_state(self):
        """Returns the current state of the game"""
        return self._current_state

    def make_move(self, current_player, user_input):
        """Returns the moves of the two players"""
        if user_input not in self._valid_choices or self._current_state != "UNFINISHED":
            return False

        if current_player == "first":
            self._input_number.append(user_input)
            self._first_list.append(user_input)
            self._valid_choices.remove(user_input)
            return True
        else:
            self._input_number.append(user_input)
            self._second_list.append(user_input)
            self._valid_choices.remove(user_input)
            return True

    def get_current_player_input(self, current_player):
        """Asks for player input, checks for valid moves"""
        if current_player == "first":
            user_input = int(input("First: "))
            if game.make_move("first", user_input):
                if self.check_if_winner():
                    if sum(self._first_list) == 15:
                        self._current_state = "FIRST_WON"
                        self.end_of_game()
                else:
                    self.get_current_player_input("second")

            else:
                print("That entry is invalid. Try again.")
                self.get_current_player_input(current_player)

        if current_player == "second":
            user_input = int(input("Second: "))
            if game.make_move("second", user_input):
                if self.check_if_winner():
                    if sum(self._second_list) == 15:
                        self._current_state = "SECOND_WON"
                        self.end_of_game()
                else:
                    self.get_current_player_input("first")
            else:
                print("That entry is invalid. Try again.")
                self.get_current_player_input(current_player)

    def check_if_winner(self):
        """Checks for winner vs draw state"""
        if sum(self._first_list) == 15 or sum(self._second_list) == 15:
            return True
        elif (sum(self._first_list) > 15 and sum(self._second_list) > 15) or len(self._valid_choices) == 0:
            self._current_state = "DRAW"
            self.end_of_game()
            return True
        else:
            return False

    def end_of_game(self):
        """Returns state of game"""
        if self._current_state == "UNFINISHED":
            print("Sorry, this game is unfinished.")

        if self._current_state == "FIRST_WON":
            print("Player 1 is the winner. Player 2 is a loser.")

        if self._current_state == "SECOND_WON":
            print("Player 2 is the winner. Player 1 is a loser.")

        if self._current_state == "DRAW":
            print("This ended in a tie. Nobody wins.")


game = AddThreeGame()
