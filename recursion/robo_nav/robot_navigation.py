"""Search function states the rules of the robot's navigation."""
from recursion.robo_nav.path import Path

POINT_IN_PATH = 'O'
TRIED = '.'
OBSTACLE = '+'
DEAD_END = '-'


def search_rule(env, start_row, start_column):
    env.update_position(start_row, start_column)
    # Check for base cases
    # 1st. If there is an obstacle in the env, return False
    if env[start_row][start_column] == OBSTACLE:
        return False
    # 2nd. If it encounters a env or point that it has previously explored
    if env[start_row][start_column] == TRIED:
        return False
    # 3rd. If the outside edge of the next move point  isn't surrounded by an
    # obstacle then it is considered a successful move
    if env.is_exit(start_row, start_column):
        env.update_position(start_row, start_column, POINT_IN_PATH)
        return True
    env.update_position(start_row, start_column, TRIED)

    # Alternatively, use logical short circuiting to try each direction in
    # turn if needed
    found = search_rule(env, start_row - 1, start_column) or \
        search_rule(env, start_row + 1, start_column) or \
        search_rule(env, start_row, start_column - 1) or \
        search_rule(env, start_row, start_column + 1)
    if found:
        env.update_position(start_row, start_column, POINT_IN_PATH)
    else:
        env.update_position(start_row, start_column, DEAD_END)
    return found


maze = Path('maze2.txt')
maze.draw_env()
maze.update_position(maze.start_row, maze.start_column)
search_rule(maze, maze.start_row, maze.start_column)
