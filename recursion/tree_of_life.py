import turtle

"""Visualizing recursion with turtle graphics"""


def tree_of_life(tree, breadth, height):
    """Call other functions to draw tree."""
    grow_trunk(tree, breadth, height)
    grow_branches(tree, breadth, height)


def grow_trunk(tree, breadth, height):
    tree.color('brown')
    tree.begin_fill()
    tree.setheading(0)
    tree.forward(breadth)
    tree.right(90)
    tree.forward(height)
    tree.right(90)
    tree.forward(breadth)
    tree.right(90)
    tree.forward(height)
    tree.end_fill()


def grow_branches(tree, breadth, height, triangles=3):
    """Draws the triangles that make up the branches and leaves of the tree."""
    tree.color('green')
    for branch in range(triangles):
        grow_leave(tree, breadth, height)
        height_increase = height / 2
        tree.sety(tree.ycor() + height_increase)


def grow_leave(tree, breadth, height):
    branch_connect = height  # The length the branch overhangs from the trunk
    leave_height = 2 * height  # Because the tree is a fir tree (christmas
    # tree) the shape will be in form of a triangle. Hence, a single triangle
    # will be 2x as tall as the trunk

    tree.begin_fill()

    x_init, y_init = (tree.xcor(), tree.ycor())
    x_center = x_init + breadth / 2.0
    x_bottom_left = x_init - branch_connect
    x_bottom_right = x_init + breadth + branch_connect
    y_top = y_init + leave_height

    tree.goto(x_bottom_left, y_init)
    tree.goto(x_center, y_top)
    tree.goto(x_bottom_right, y_init)
    tree.goto(x_init, y_init)

    tree.end_fill()


breadth = 45
height = 90

tree = turtle.Turtle()
tree_of_life(tree, breadth, height)
turtle.done()
