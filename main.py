import turtle
def draw_square(size):
    for i in range(4):
        turtle.forward(size)
        turtle.right(90)
draw_square(100)
turtle.forward(50)
turtle.right(45)
draw_square(71)

turtle.exitonclick()