class Ant:

    def __init__(self):
        self._size_x = 13  # size of grid
        self._size_y = 13  # size of grid
        self._direction = 0
        self._initial_grid = [[0] * self._size_x for i in range(self._size_y)]
        self._direction = 0
        self._grid = []
        self._move = 0
        self._required_moves = 100
        self._ant_x = 5  # pos
        self._ant_y = 5  # pos
        self._get_input_grid_size()
        self._get_ant_starting_pos()
        self._get_ant_orientation()
        self._get_ant_steps()
        self._move_ant()

    def _get_input_grid_size(self):
        _grid_size = int(input("Please enter a number no larger than 100 for the size of the square board:  "))
        self._size_x = _grid_size
        self._size_y = _grid_size

        self._grid_builder()

    def _get_ant_starting_pos(self):
        self._ant_x = int(input("Please enter a number as the starting row number: "))
        self._ant_y = int(input("Please enter a number as the starting column number : "))

    def _get_ant_orientation(self):
        self._direction = int(input("Please choose the ant’s starting orientation:  "))

    def _get_ant_steps(self):
        self._move = int(input("Please enter the number of steps for the simulation : "))

    def _grid_builder(self):
        self._grid = [[0] * self._size_x for i in range(self._size_y)]

    def _move_up(self):
        """move ant in proper direction"""
        self._ant_x = self._ant_x - 1
        if self._ant_x < 0:
            self._ant_x = self._size_x - 1

    def _move_right(self):
        """move ant in proper direction"""
        self._ant_y = self._ant_y + 1
        if self._ant_y > self._size_y - 1:
            self._ant_y = 0

    def _move_down(self):
        """move ant in proper direction"""
        self._ant_x = self._ant_x + 1
        if self._ant_x > self._size_x - 1:
            self._ant_x = 0

    def _move_left(self):
        """move ant in proper direction"""
        self._ant_y = self._ant_y - 1
        if self._ant_y < 0:
            self._ant_y = self._size_y - 1

    def _turn_right(self, last_direction):
        """direction change"""
        new_direction = last_direction + 1
        if last_direction == 3:
            new_direction = 0
        return new_direction

    def _turn_left(self, last_direction):
        """direction change"""
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
        """Move function"""
        if self._required_moves > self._move:
            self._check_and_update_direction()
            if self._direction == 0:
                self._move_up()
            elif self._direction == 1:
                self._move_right()
            elif self._direction == 2:
                self._move_down()
            elif self._direction == 3:
                self._move_left()

            # incrementing the move counter
            self._move = self._move + 1
            self._grid[self._ant_x][self._ant_y] = 1 if self._grid[self._ant_x][self._ant_y] == 0 else 0
            if self._move % 10 == 0:
                print()
                self._render()
                print()
            self._move_ant()
        else:
            self._render()

    def _render(self, _grid=None):
        """start of render function"""
        new_grid = list(map(list, self._grid))
        new_grid[self._ant_x][self._ant_y] = 8
        for x in new_grid:
            for y in x:
                # white = "_"
                white = "　"
                # black = "#"
                black = "○"
                # cur_pos = "8"
                cur_pos = "●"
                if y == 0 and y != 8:
                    position = white
                elif y == 8:
                    position = cur_pos
                else:
                    position = black
                print(position, end="")
            print(end="\n")

    def run_stimulation(self):
        self._move_ant()


ant = Ant()
