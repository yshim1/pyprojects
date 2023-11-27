from turtle import Turtle, Screen, colormode
import random

# Used to extract colors 
# import colorgram

# colors = colorgram.extract('/Users/yamlak/Downloads/dots.jpg', 40)
# colorList = []
# for color in colors:
#     colorList.append(tuple(color.rgb))
# print(colorList)

t = Turtle()
colormode(255)
A = [(207, 160, 82), (54, 88, 130), (145, 91, 40), (140, 26, 49), (221, 207, 105), (132, 177, 203), (158, 46, 83), 
    (45, 55, 104), (169, 160, 39), (129, 189, 143), (83, 20, 44), (37, 43, 67), (186, 94, 107), (187, 140, 170), (85, 120, 180), 
    (59, 39, 31), (88, 157, 92), (78, 153, 165), (194, 79, 73), (45, 74, 78), (80, 74, 44), (161, 201, 218), (57, 125, 121), 
    (219, 175, 187), (169, 206, 172), (219, 182, 169), (179, 188, 212), (48, 74, 73), (147, 37, 35), (43, 62, 61)]
number_of_dots = 100
t.hideturtle()
t.speed('fastest')
t.setheading(225)
t.penup()
t.forward(300)
t.setheading(0)
for dot_count in range(1, number_of_dots + 1):
    t.dot(20, random.choice(A))
    t.penup()
    t.forward(50)
    if dot_count % 10 == 0:
        t.setheading(90) # faces north after completing 10
        t.forward(50) # moves 50 units of space from  last row
        t.setheading(180) # sets direction ot left
        t.forward(500) # moves forward 500 units
        t.setheading(0) # sets direction to right to continue outer loop
    
    

s = Screen()
s.exitonclick()
