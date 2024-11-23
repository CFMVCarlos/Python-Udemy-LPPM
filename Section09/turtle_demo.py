# import turtle
# turtle.forward(150)
# turtle.right(250)
# turtle.forward(150)
# turtle.done()

from turtle import circle, done, forward, right

side_a: float = 150
side_b: float = 150
side_c: float = (side_a**2 + side_b**2) ** 0.5


for _ in range(8):
    forward(side_a)
    right(90)
    forward(side_b)
    right(90 + 45)
    forward(side_c)
    circle(75)

done()
