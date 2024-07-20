import turtle as t
turtle = t.Turtle()
"""turtle.color ("red") 
turtle.forward ( 100)
turtle.right(90)
turtle.forward ( 100)
turtle.right (90)
turtle.forward ( 100)
turtle.right (90)
turtle.forward ( 100)
my_color = ["red", "blue", "green","orange","yellow", "purple"]
for i in range (300):
    turtle.color(my_color[i % 6 ])
    turtle.forward (i +10)
    turtle.right (91)
    turtle.width (i /100 + 5)"""
my_color = ["red", "blue", "green","orange","yellow", "purple"]
for x in range (1,19):
    turtle.color(my_color[x % 6])
    turtle.forward (100)
    if (x % 2 == 0):
        turtle.left (175)
    else:
        turtle.left(225) 
    
