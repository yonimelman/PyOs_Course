import turtle
import random


def spiral_squared(size):
	s = turtle.Screen()
	t = turtle.Turtle()
	t.pensize(3)

	for i in range(size,0,-4):
		t.forward(i)
		t.right(90)
		t.pencolor(random.random(),random.random(),random.random())
		
	s.exitonclick()
