import turtle 

def draw_rectangle(t, width, height):
    for _ in range(2):
        t.forward(width)
        t.left(90)
        t.forward(height)
        t.left(90)

# Function to draw a triangle
def draw_triangle(t, size):
    for _ in range(3):
        t.forward(size)
        t.left(120)

# Function to draw a door
def draw_door(t):
    t.penup()
    t.goto(-40, -150)
    t.pendown()
    t.setheading(0)  # Set the turtle's heading to the right
    draw_rectangle(t, 80, 100)

# Function to draw a window
def draw_window(t):
    t.penup()
    t.goto(80, -50)
    t.pendown()
    t.setheading(0)  # Set the turtle's heading to the right
    draw_rectangle(t, 60, 60)

# Function to draw a balcony
def draw_balcony(t):
    t.penup()
    t.goto(-120, 50)
    t.pendown()
    t.setheading(0)  # Set the turtle's heading to the right
    draw_rectangle(t, 240, 20)
    t.penup()
    t.goto(-100, 50)
    t.pendown()
    draw_rectangle(t, 200, 100)

# Function to draw the house
def draw_house():
    # Create a Turtle object
    house = turtle.Turtle()
    house.speed(0)  # Set the fastest drawing speed

    # Draw the first floor
    draw_rectangle(house, 200, 200)

    # Draw the second floor
    house.penup()
    house.goto(-90, 0)
    house.pendown()
    draw_rectangle(house, 180, 150)

    # Draw the roof
    house.penup()
    house.goto(-100, 200)
    house.pendown()
    draw_triangle(house, 400)

    # Draw the door
    draw_door(house)

    # Draw the window
    draw_window(house)

    # Draw the balcony
    draw_balcony(house)

    # Hide the turtle
    house.hideturtle()

    # Keep the window open until it's manually closed
    turtle.done()

# Call the function to draw the house
draw_house()


















































































































exitonclick()