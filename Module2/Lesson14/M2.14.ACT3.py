import turtle # Importing Library 
my_wn = turtle.Screen()
my_wn.bgcolor("light blue") # Screen Background Colour
my_wn.title("Turtle")
my_pen = turtle.Turtle()

size = 0
while True: # Iterate Loop to automate
    for i in range(4):
        my_pen.forward(size + 1)
        my_pen.left(90)
        size = size - 5
    size = size + 1
    