from turtle import *

bgcolor('blue')

speed(10)
setup(800,500)

penup()
goto(-400, -250)
pendown()

color('yellow')
begin_fill()
forward(800)
left(90)
forward(250)
left(90)
forward(800)
end_fill()

hideturtle()
exitonclick()