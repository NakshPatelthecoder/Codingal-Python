import turtle   # Importing Library
turtle.Screen().bgcolor("Orange")
turtle.Screen().setup(300,400)
polygon = turtle.Turtle() # defined variable

num_sides = int(input(" Enter a number of sides for your polygon (Must be 3 or more): "))
side_length = 70
angle = 360.0 / num_sides
# Iterate loop for total number of sides
for i in range(num_sides):
    polygon.forward(side_length)
    polygon.right(angle)


turtle.done()