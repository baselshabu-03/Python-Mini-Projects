import turtle

screen = turtle.Screen()
screen.bgcolor("blue")
screen.title("Drawing Lines")

my_turtle = turtle.Turtle()
my_turtle.pensize(5)
my_turtle.color("green")
my_turtle.fillcolor("red")
my_turtle.begin_fill()
my_turtle.circle(100)
my_turtle.end_fill()

turtle.done()