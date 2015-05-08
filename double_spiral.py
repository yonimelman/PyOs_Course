import turtle

t = turtle.Turtle()
s = turtle.Screen()

size= 100
for i in range(1,3):
    for j in range(1,size+1):
        
        if i%2 != 0:
            t.right(30)
            t.forward(j/2)
        else:
            t.left(30)
            t.forward((size-j)/2)


s.exitonclick()
