from turtle import Turtle, Screen
import random

POINTS = {
    "A": (0, 300),
    "B": (-300, -300),
    "C": (300, -300),
}

screen = Screen()
screen.title("Sierpinski Triangle")
screen.setup(800, 800)
screen.tracer(0)

marker = Turtle()
marker.hideturtle()
marker.penup()

def create_points():
    points = []
    for point in POINTS:
        new_point = Turtle()
        new_point.penup()
        new_point.hideturtle()
        new_point.goto(POINTS[point])
        new_point.dot(5, "blue")
        points.append(point)
    return points

def paint(points):
    random_point = random.choice(points)
    point_position = POINTS[random_point]
    marker_position = (marker.xcor(), marker.ycor())
    new_marker_position_x = (point_position[0] + marker_position[0])/2
    new_marker_position_y = (point_position[1] + marker_position[1])/2
    new_marker_position = (new_marker_position_x, new_marker_position_y)
    marker.goto(new_marker_position)
    marker.dot(2, "black")

all_points = create_points()
while True:
    for _ in range(1000):
        paint(all_points)
    screen.update()
