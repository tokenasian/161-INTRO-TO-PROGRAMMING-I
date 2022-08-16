# Author: Matthew Armstrong
# Date: 08/12/2021
# Description: Langton Ant stimulation program.
class Ant:
    """represents the ant class"""
    def __init__(self):
        """private ant classes"""
        self._size_x = 0  # grid size
        self._size_y = 0  # grid size
        self._direction = 0  # ant starting direction
        self._grid = []
        self._move = 0  # move counter
        self._required_moves = 100  # number of moves to make from user
        self._ant_x = 5  # pos
        self._ant_y = 5  # pos

    def _get_input_grid_size(self):
        """get the grid size"""
        print("Welcome to Langton’s ant simulation!")
        _grid_size = int(input(
            "Please enter a number no larger than 100 for the size of the square board:  "))
        self._size_x = _grid_size
        self._size_y = _grid_size

        self._grid_builder()

    def _validate_grid_size(self):
        """validate the grid size"""
        if self._size_x + 1 > 100 or self._size_x < 0:
            print(
                "invalid grid size input, number must be positive and must be under 100")
            self._get_input_grid_size()

    def _get_ant_starting_pos(self):
        """get the ant starting position"""
        self._ant_x = int(
            input("Please enter a number as the starting row number: "))
        self._ant_y = int(
            input("Please enter a number as the starting column number : "))

    def _validate_ant_starting_pos(self):
        """validate the ant position"""
        if self._ant_x > self._size_x - 1 or self._ant_y > self._size_y - 1 or self._ant_x < 0 or self._ant_y < 0:
            print("Ant starting position was invalid")
            self._get_ant_starting_pos()

    def _get_ant_orientation(self):
        """get the ant orientation"""
        self._direction = int(
            input("Please choose the ant’s starting orientation:  "))

    def _get_ant_steps(self):
        """get the number of steps for the ant"""
        self._required_moves = int(
            input("Please enter the number of steps for the simulation : "))

    def _grid_builder(self):
        """make the grid"""
        self._grid = [[0] * self._size_x for i in range(self._size_y)]

    def _move_up(self):
        """move the ant in the proper direction"""
        self._ant_x = self._ant_x - 1
        if self._ant_x < 0:
            self._ant_x = self._size_x - 1

    def _move_right(self):
        """move the ant in the proper direction"""
        self._ant_y = self._ant_y + 1
        if self._ant_y > self._size_y - 1:
            self._ant_y = 0

    def _move_down(self):
        """move the ant in the proper direction"""
        self._ant_x = self._ant_x + 1
        if self._ant_x > self._size_x - 1:
            self._ant_x = 0

    def _move_left(self):
        """move the ant in the proper direction"""
        self._ant_y = self._ant_y - 1
        if self._ant_y < 0:
            self._ant_y = self._size_y - 1

    def _turn_right(self, last_direction):
        """make the ant change direction"""
        new_direction = last_direction + 1
        if last_direction == 3:
            new_direction = 0
        return new_direction

    def _turn_left(self, last_direction):
        """make the ant change direction"""
        new_direction = last_direction - 1
        if last_direction == 0:
            new_direction = 3
        return new_direction

    def _check_and_update_direction(self):
        """check if grid is black or white then turn proper direction"""
        if self._grid[self._ant_x][self._ant_y] == 0:
            self._direction = self._turn_right(self._direction)
        else:
            self._direction = self._turn_left(self._direction)

    def _move_ant(self):
        """make the ant move"""
        if self._required_moves >= self._move:
            if self._move != -1:
                self._check_and_update_direction()
            if self._direction == 3:
                self._move_up()
            elif self._direction == 0:
                self._move_right()
            elif self._direction == 1:
                self._move_down()
            elif self._direction == 2:
                self._move_left()

            # incrementing the move counter
            self._move = self._move + 1
            self._grid[self._ant_x][self._ant_y] = 1 if self._grid[self._ant_x][self._ant_y] == 0 else 0
            self._move_ant()
        else:
            self._print_board()

    def _print_board(self, _grid=None):
        """print board function to display the board"""
        new_grid = list(map(list, self._grid))
        new_grid[self._ant_x][self._ant_y] = 8
        print("")
        for x in reversed(new_grid):
            for y in x:
                white = "_"
                black = "#"
                cur_pos = "8"
                if y == 0 and y != 8:
                    position = white
                elif y == 8:
                    position = cur_pos
                else:
                    position = black
                print(position, end="")
            print(end="\n")

    def run_simulation(self):
        """run ant simulation function"""
        self._get_input_grid_size()  # board size
        self._validate_grid_size()
        self._get_ant_starting_pos()  # row and column
        self._validate_ant_starting_pos()
        self._get_ant_orientation()  # starting direction
        self._get_ant_steps()  # number of moves to make from user

    def main(self):
        """main function"""
        self._move_ant()


ant = Ant()
ant.run_simulation()
ant.main()
