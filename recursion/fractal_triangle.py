"""The code in the script is used to draw a Sierpinski Triangle"""

import turtle


def draw_triangle(points, color, draw_init):
    """Specifies the parameters for the triangle."""
    draw_init.fillcolor(color)
    draw_init.up()
    draw_init.goto(points[0])
    draw_init.down()
    draw_init.begin_fill()
    draw_init.goto(points[1])
    draw_init.goto(points[2])
    draw_init.goto(points[0])
    draw_init.end_fill()


def get_center(pos1, pos2):
    return (pos1[0] + pos2[0]) / 2, (pos1[1] + pos2[1]) / 2


def sierpinski(points, degree, draw_init):
    """Main function that runs the program"""
    colormap = ['blue', 'red', 'purple', 'brown', 'yellow', 'orange', 'pink',
                'white', 'black']

    draw_triangle(points, colormap[degree], draw_init)
    if degree > 0:
        sierpinski([points[0], get_center(points[0], points[1]), get_center(
            points[0], points[2])], degree - 1, draw_init)
        sierpinski([points[1], get_center(points[0], points[1]), get_center(
            points[1], points[2])], degree - 1, draw_init)
        sierpinski([points[2], get_center(points[2], points[1]), get_center(
            points[0], points[2])], degree-1, draw_init)


draw_init = turtle.Turtle()
draw_points = [(-500, -250), (0, 500), (500, -250)]
sierpinski(draw_points, 4, draw_init)
turtle.done()
