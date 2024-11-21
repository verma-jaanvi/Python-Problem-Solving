import turtle

screen = turtle.Screen()
t = turtle.Turtle()
t.speed(0.2)

def draw_circle(radius, color, x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color(color)
    t.begin_fill()
    t.circle(radius)
    t.end_fill()

def draw_square(size, color, x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color(color)
    t.begin_fill()
    for _ in range(4):
        t.forward(size)
        t.right(90)
    t.end_fill()

def draw_rectangle(width, height, color, x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color(color)
    t.begin_fill()
    for _ in range(2):
        t.forward(width)
        t.right(90)
        t.forward(height)
        t.right(90)
    t.end_fill()

def draw_triangle(size, color, x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color(color)
    t.begin_fill()
    for _ in range(3):
        t.forward(size)
        t.left(120)
    t.end_fill()

def draw_doll():
    draw_circle(50, 'orange', 0, 0)  # Head

    draw_rectangle(80, 120, 'green', -40, 0)  # Body

    draw_rectangle(20, 60, 'blue', -30, -120)  # Left leg
    draw_rectangle(20, 60, 'blue', 10, -120)   # Right leg

    draw_rectangle(20, 60, 'yellow', -60, 0)   # Left arm
    draw_rectangle(20, 60, 'yellow', 40, 0)    # Right arm

    draw_triangle(100, 'red', -50, 70)  # Hat

draw_doll()

t.hideturtle()
screen.mainloop()
