from turtle import Turtle, Screen
import random

# tim = Turtle()
screen = Screen()
screen.setup(height=400, width=500)

is_race_on = False

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtles = []

user_bet = screen.textinput(title="Turtle Race", prompt="Which turtle will win the race? Enter a color: ")
# print(user_bet)

winning_turtle_color = ""

if user_bet:
    is_race_on = True

x = -230
y = -70

for i in range(len(colors)):
    turtle = Turtle(shape="turtle")
    turtle.penup()
    turtle.color(colors[i])
    turtle.goto(x=x, y=y)
    y += 30
    turtles.append(turtle)

while is_race_on:
    for turtle in turtles:
        if turtle.xcor() > 230:
            winning_turtle_color = turtle.pencolor()
            is_race_on = False

        turtle.forward(random.randint(0, 10))

if user_bet == winning_turtle_color:
    print(f"You Won! The winner is {winning_turtle_color} Turtle")
else:
    print(f"You Lose! The winner is {winning_turtle_color} Turtle")


screen.exitonclick()
