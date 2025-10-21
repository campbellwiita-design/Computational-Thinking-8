import turtle
t = turtle.Turtle()
# used to have a teleporting line here changed it becuase got feed back to get rid of black line

turtle.Screen().bgcolor("Lavender") # used to not have backround got feedback to add one
colors = ["pink","cyan","yellow"] # used to be gray, got feedback to change to yellow
for i in range (500) :
    t.color( colors[i % 3 ] )
    t.forward(100 + i)
    t.left(120-1)

turtle.exitonclick ()