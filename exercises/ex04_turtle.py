"""A lovely day outside!"""

__author__ = "730410153"

from turtle import Turtle, colormode, done


def main() -> None:
    """The entrypoint of my scene."""
    grass(-350, -30)
    sun(250, 300)
    cloud(150, 230)
    bird(100, 100)
    bird(50, 100)
    bird(0, 100)


def grass(x: int, y: int) -> None:
    "The scene starts with soome grass for the animals."
    grass: Turtle = Turtle()
    colormode(255)
    grass.color("green")
    grass.color(75, 100, 92)
    grass.fillcolor(108, 237, 171)

    grass.penup()
    grass.goto(x, y)
    grass.pendown()

    grass.begin_fill()

    i: int = 0

    while (i < 10):
        if (i % 2 == 0):
            grass.forward(80)
            grass.right(45)
        else:
            grass.forward(80)
            grass.left(45)
        i += 1

    grass.end_fill()
    grass.speed(50)


def sun(x: int, y: int) -> None:
    """Then, the sun comes out to wake everyone."""
    sun: Turtle = Turtle()
    colormode(255)
    sun.color("yellow")
    sun.color(251, 246, 130)
    sun.fillcolor(251, 246, 130)

    sun.penup()
    sun.goto(x, y)
    sun.pendown()

    sun.begin_fill()

    i: int = 0
    while (i < 4):
        sun.forward(90)
        sun.right(90)
        i += 1

    sun.end_fill()

    sun.speed(50)


def cloud(x: int, y: int) -> None:
    """A cloud arrives to provide some shade."""
    cloud: Turtle = Turtle()
    colormode(255)
    cloud.color("blue")
    cloud.color(130, 229, 251)
    cloud.fillcolor(130, 229, 251)

    cloud.penup()
    cloud.goto(x, y)
    cloud.pendown()

    cloud.begin_fill()

    i: int = 0
    while (i < 70):
        cloud.forward(5)
        cloud.right(5)
        i += 1

    cloud.end_fill()
    cloud.speed(50)


def bird(x: int, y: int) -> None:
    """The first bird shows up. The bird has wings using the backward feature!"""
    bird: Turtle = Turtle()
    colormode(255)
    bird.color("black")
    bird.color(38, 63, 69)
    bird.pencolor("orange")
    bird.pencolor(249, 171, 38)

    bird.penup()
    bird.goto(x, y)
    bird.pendown()

    bird.backward(40)
    bird.right(45)
    bird.forward(75)
    bird.right(90)
    bird.forward(75)
    bird.left(120)
    bird.forward(40)

    bird.speed(50)


if __name__ == "__main__":
    main()