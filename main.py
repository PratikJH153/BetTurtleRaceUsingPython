from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forward():
    tim.forward(10)


def move_backward():
    tim.backward(10)


def turn_left():
    # tim.left(5)
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)


def turn_right():
    # tim.right(5)
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)


def clear_screen():
    tim.clear()
    # tim.setposition(0, 0)
    tim.penup()
    tim.home()
    tim.pendown()
    

screen.listen()

screen.onkeypress(key="w", fun=move_forward)
screen.onkeypress(key="s", fun=move_backward)
screen.onkeypress(key="a", fun=turn_left)
screen.onkeypress(key="d", fun=turn_right)
screen.onkeypress(key="c", fun=clear_screen)


screen.exitonclick()
