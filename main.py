import turtle as turtle_module
import random

t = turtle_module.Turtle()
turtle_module.colormode(255)

color_list = [(202, 164, 110), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]

t.speed("fastest")
t.hideturtle()
t.penup()
t.setposition(-250, -200)


# Method1 :
# Starting from left
def change_position():
    initial_pos = t.ycor()
    space = 50
    t.setposition(-250, initial_pos + space)


def dotted_line():
    for _ in range(10):
        t.dot(20, random.choice(color_list))
        t.forward(50)


for _ in range(10):
    dotted_line()
    change_position()


# Method 2:
# Starting from where its left
def dotted_line():
    for _ in range(10):
        t.dot(20, random.choice(color_list))
        t.forward(50)


def lift_right():
    for _ in range(2):
        t.left(90)
        t.forward(50)


def lift_left():
    for _ in range(2):
        t.right(90)
        t.forward(50)


for _ in range(5):
    dotted_line()
    lift_right()
    dotted_line()
    lift_left()


screen = turtle_module.Screen()
screen.exitonclick()
