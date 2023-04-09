import turtle

pen = turtle.Turtle()

colors = ['blue', 'cyan', 'green', 'yellow', 'red', 'magenta']
pen.speed('fastest')

N = 4  # The factor by which each recursive side is scaled down by
S = 5  # The number of sides in the shape
angle = 180 / S  # Interior angle in star


def star(length: int, depth: int):
    """
star(length, depth) is a function that draws a star on the Turtle Canvas
length: int; represents the length of each side, in pixels. This length is divided by N for each recursive call.
depth: int; represents the maximum depth of the fractal
"""
    if depth == 1:  # a base case to make the program terminate. theoretically, there is no base case
        return 0
    for _ in range(S):
        pen.color(colors[depth % len(
            colors)])  # ensures that different depths are colored differently so that it is visually clear
        pen.forward(length)
        star(length // N, depth - 1)  # a recursive call with length divided by N and depth decreased by 1
        pen.right(180 - angle)


pen.left(90 - angle // 2)  # setting up the initial angle
star(200, 5)  # call to render a star
pen.hideturtle()
