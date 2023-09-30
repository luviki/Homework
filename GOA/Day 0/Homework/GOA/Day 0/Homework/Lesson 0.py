from turtle import *

#we want to build a house

#Step 1: Draw a square
speed(50)
width(5)
color("black")
begin_fill()
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
end_fill()
#End of square

forward(70)
color("red")
left(90)
forward(120) #heigth of the door
right(90)
forward(60)
right(90)
forward(120)
left(180)
forward(50)
left(90)
forward(10)
#end of the door

penup()
goto(200, 200)
pendown()

color("red")
begin_fill()
right(60)
forward(200)
left(120)
forward(200)
end_fill()
#end of the roof

penup()
goto(0, 100)
pendown()

color("yellow")
begin_fill()
left(120)
forward(50)
left(90)
forward(50)
left(90)
forward(50)
end_fill()

penup()
goto(200, 150)
pendown()

color("yellow")
begin_fill()
forward(50)
left(90)
forward(50)
left(90)
forward(50)
end_fill()
#Welcome to my house

exitonclick()
