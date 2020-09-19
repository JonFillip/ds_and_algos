from turtle import Turtle, Screen

"""The Path class describes the attributes and features of a maze or physical
environment that a robot will interact with."""
POINT_IN_PATH = 'O'
TRIED = '.'
OBSTACLE = '+'
DEAD_END = '-'


class Path:
    def __init__(self, maze_env):
        """In the environment, it is rendered as a grid with rows and columns"""
        columns_in_env = 0
        self.gridlist = []
        env_file = maze_env
        with open(env_file) as maze_file:
            rows_in_env = 0
            for line in maze_file:
                row_list = []
                col = 0
                for ch in line[:-1]:
                    row_list.append(ch)
                    if ch == 'M':
                        self.start_row = rows_in_env
                        self.start_column = col
                    col += 1
                rows_in_env += 1
                self.gridlist.append(row_list)
                columns_in_env = len(row_list)

        self.row_in_env = rows_in_env
        self.columns_in_env = columns_in_env
        self.xRoute = -columns_in_env / 2
        self.yRoute = rows_in_env / 2
        self.draw = Turtle(shape='turtle')
        self.screen = Screen()
        self.screen.setup(width=600, height=600)
        self.screen.setworldcoordinates(-(columns_in_env - 1) / 2 - .5,
                                        -(rows_in_env - 1) / 2 - .5,
                                        (columns_in_env - 1) / 2 + .5,
                                        (rows_in_env - 1) / 2 + .5)

    def draw_env(self):
        """Draws out the environment or space the robot is to navigate
        through."""
        for y in range(self.row_in_env):
            for x in range(self.columns_in_env):
                if self.gridlist == OBSTACLE:
                    self.draw_center_box(x + self.xRoute, -y + self.yRoute,
                                         'tan')

        self.draw.color('black', 'blue')

    def draw_center_box(self, x, y, color):
        self.screen.tracer(0)
        self.draw.up()
        self.draw.goto(x - .5, y - .5)
        self.draw.color('black', color)
        self.draw.setheading(90)
        self.draw.down()
        self.draw.begin_fill()
        for dot in range(4):
            self.draw.forward(1)
            self.draw.right(90)
        self.draw.end_fill()
        self.screen.update()
        self.screen.tracer(1)

    def move_drawing(self, x, y):
        """Draws up the robot on the as it moves"""
        self.draw.up()
        self.draw.setheading(
            self.draw.towards(x + self.xRoute, -y + self.yRoute))
        self.draw.goto(x + self.xRoute, -y + self.yRoute)

    def leave_trails(self, color):
        """Leaves a colored trail of where the robot has been"""
        self.draw.dot(color)

    def update_position(self, row, col, value=None):
        """Updates the robots position as it moves"""
        if value:
            self.gridlist[row][col] = value
        self.move_drawing(col, row)

        if value == POINT_IN_PATH:
            color = 'green'

        elif value == OBSTACLE:
            color = 'red'

        elif value == TRIED:
            color = 'black'

        elif value == DEAD_END:
            color = 'red'
        else:
            color = None

        if color:
            self.leave_trails(color)

    def is_exit(self, row, col):
        return (
            row == 0 or
            row == self.row_in_env - 1 or
            col == 0 or
            col == self.columns_in_env - 1
        )

    def __getitem__(self, item):
        return self.gridlist[item]
