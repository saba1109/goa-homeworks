from turtle import *

#paint a house

#step 1: draw a square
speed(10)
width(7)
color("blue")
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
#end of square

#drawing a door
begin_fill()
forward(70)
color("black")
left(90)
forward(120)     #height of the door
right(90)
forward(60)
right(90)
forward(120)


penup()
goto(200, 200)
pendown()

color("red")
right(150)
forward(200)
left(120)
forward(200)

#drawing windows
penup()
goto(0, 130)
pendown()
left(120)
forward(40)
left(90)
forward(65)


penup()
goto(0, 160)
pendown()
right(90)
forward(40)
penup()
goto(22, 200)
pendown()

right(90)
forward(71)

#second window
penup()
goto(200, 130)
pendown()
right(90)
forward(40)
right(90)
forward(65)
right(90)
forward(40)

penup()
goto(200, 160)
pendown()
right(180)
forward(40)

penup()
goto(180, 190)
pendown()

left(90)
forward(55)


exitonclick()