import turtle # importing the turtle module

window = turtle.Screen() # creating a Screen instance
t = turtle.Turtle() # creating a Turtle instance

# Moving the turtle to the top-left corner of the screen
t.penup()
t.setposition(-200,200)
t.pendown()

# starting the stairs sequence
for i in range(1,50):
    if i % 2 == 0:
        t.left(90)
    elif i % 2 != 0:
        t.right(90)
    
    t.forward(10)
    

window.exitonclick()
