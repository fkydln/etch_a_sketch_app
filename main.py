from turtle import Turtle, Screen

faz = Turtle()
screen = Screen()
faz.setheading(90)


def move_forwards():
    faz.forward(10)


def move_backwards():
    faz.backward(10)


def heading_left():
    faz.left(10)


def heading_right():
    faz.right(10)


def screen_clear():
    faz.clear()
    faz.penup()
    faz.home()
    faz.pendown()
    faz.setheading(90)


screen.listen()

screen.onkey(move_forwards, "w")
screen.onkey(move_backwards, "s")
screen.onkey(heading_left, "a")
screen.onkey(heading_right, "d")
screen.onkey(screen_clear, "c")
screen.exitonclick()
