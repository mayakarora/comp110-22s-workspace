from turtle import Turtle, colormode, done
leo: Turtle = Turtle()
colormode(255)
leo.color("green")
leo.color(108, 237, 171)
leo.fillcolor(108, 237, 171)

leo.penup()
leo.goto(-150, 80)
leo.pendown()

leo.begin_fill()

i: int = 0
while (i < 3):
    leo.forward(100)
    leo.right(120)
    i += 1

leo.end_fill()

leo.speed(50)
leo.hideturtle()

bob: Turtle = Turtle()
colormode(255)
bob.color("green")
bob.color(75, 100, 92)

bob.penup()
bob.goto(-300, 160)
bob.pendown()

i: int = 0
while (i < 3):
    bob.forward(400)
    bob.right(120)
    i += 1

side_length: int = 300

i: int = 0
while (i < 3):
    bob.forward(side_length)
    bob.right(120)
    i += 1
    side_length == side_length * 0.98

side_length: int = 200

i: int = 0
while (i < 3):
    bob.forward(side_length)
    bob.right(120)
    i += 1
    side_length == side_length * 0.98

side_length: int = 100

i: int = 0
while (i < 3):
    bob.forward(side_length)
    bob.right(120)
    i += 1
    side_length == side_length * 0.98

side_length: int = 50

i: int = 0
while (i < 3):
    bob.forward(side_length)
    bob.right(120)
    i += 1
    side_length == side_length * 0.98

side_length: int = 25

i: int = 0
while (i < 3):
    bob.forward(side_length)
    bob.right(120)
    i += 1
    side_length == side_length * 0.98

side_length: int = 10

i: int = 0
while (i < 3):
    bob.forward(side_length)
    bob.right(120)
    i += 1
    side_length == side_length * 0.98

side_length: int = 5

i: int = 0
while (i < 3):
    bob.forward(side_length)
    bob.right(120)
    i += 1
    side_length == side_length * 0.98

side_length: int = 3

i: int = 0
while (i < 3):
    bob.forward(side_length)
    bob.right(120)
    i += 1
    side_length == side_length * 0.98

side_length: int = 2

i: int = 0
while (i < 3):
    bob.forward(side_length)
    bob.right(120)
    i += 1
    side_length == side_length * 0.98

side_length: int = 1

i: int = 0
while (i < 3):
    bob.forward(side_length)
    bob.right(120)
    i += 1
    side_length == side_length * 0.98

bob.speed(83)
bob.hideturtle()