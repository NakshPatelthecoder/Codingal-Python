import turtle

# Get user inputs
bg_color = input("Enter background color (e.g., black, white, blue): ")
pen_color = input("Enter pen color (e.g., red, green, yellow): ")
pen_width = int(input("Enter pen width (e.g., 1, 3, 5): "))
side_length = int(input("Enter square side length (e.g., 100): "))

# Set up the screen
screen = turtle.Screen()
screen.bgcolor(bg_color)

# Create turtle
pen = turtle.Turtle()
pen.color(pen_color)
pen.width(pen_width)

# Draw square
for _ in range(4):
    pen.forward(side_length)
    pen.right(90)

# Finish
turtle.done()