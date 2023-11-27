from turtle import Turtle, Screen, colormode
import random
import colorgram


t = Turtle()
t.shape("turtle")
t.speed('fastest')
directions = [0, 90, 180, 270]
# Random color polygon from square to dec
# def draw_shape(sides):
#     angle = 360/sides
#     for i in range(sides):
#         t.forward(100)
#         t.right(angle)
# colormode(255)
# for polygon in range(3,11):
#     tup = (random.randint(1,255), random.randint(1,255), random.randint(1,255))
#     t.color(tup)
#     draw_shape(polygon)

# Dashed line
# for i in range(10):
#     t.forward(10)
#     t.penup()
#     t.forward(10)
#     t.pendown()

# Random direction colorful scramble
# colormode(255)
# t.pensize(10)
# def wall_checker():
#     #print(self.xcor(), self.ycor())
    
#     if t.xcor() > 300:
#         t.goto(290, t.ycor())
#     elif t.xcor() < -300:
#         t.goto(-290, t.ycor())

#     if t.ycor() > 300:
#         t.goto(t.xcor(), 290)
#     elif t.ycor() < -300:
#         t.goto(t.xcor(), -290)

# x = True
# for i in range(300):
#     tup = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
#     t.color(tup)
#     t.forward(30)
#     wall_checker()
#     t.setheading(random.choice(directions))

screen = Screen()
screen.exitonclick()




