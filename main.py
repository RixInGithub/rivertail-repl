import turtle

rivertailimg = "/rivertailPonyHead.svg"

paper = turtle.Screen()
paper.setup(width=480, height=360)
paper.bgcolor("White")
paper.register_shape(rivertailimg)

flippy = turtle.Turtle()
flippy.shape("turtle")

rivertail = turtle.Turtle(shape=rivertailimg)