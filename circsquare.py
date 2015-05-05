import turtle # importing the turtle module

window = turtle.Screen() # creating a Screen instance
t = turtle.Turtle() # creating a Turtle instance

i = 1 # counter variable
while i <= 36:
    # drawing a square
    t.forward(100)
    t.right(90)
    t.forward(100)
    t.right(90)
    t.forward(100)
    t.right(90)
    t.forward(100)
    t.right(90)
	# tilting it 10 degrees
    t.right(10)
    i+=1
    

window.exitonclick()