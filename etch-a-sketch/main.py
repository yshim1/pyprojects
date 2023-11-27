"""
The goal of this project is to demonstrate knowledge of higher order functions (functions that take functions as input or output), 
event listeners, and passing functions as arguments
"""


from turtle import Turtle, Screen

t = Turtle()
s = Screen()
s.listen()

def move_forward():
    t.forward(10)
def move_backward():
    t.backward(10)
def clockwise():
    t.setheading(t.heading() + 5)
def counterClocwise():
    t.setheading(t.heading() + 5)
def clear():
    t.clear()
s.onkey(key='w', fun=move_forward)
s.onkey(key='s', fun=move_backward)
s.onkey(key='d', fun=clockwise)
s.onkey(key='a', fun=counterClocwise)
s.onkey(key='c', fun=clear)

s.exitonclick()