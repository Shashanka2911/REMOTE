from turtle import*
title("FUNNY")
bgcolor("black")
speed(0)
pensize(3)
for i in range(9):
    color("blue")
    left(60)
    circle(-18,200)
    color("green","yellow")
    r=100
    for j in range(12):
        begin_fill()
        circle(r-11*j,90)
        end_fill
    left(180)
    penup()
    goto(0,0)
    pendown()    
    hideturtle()
done()