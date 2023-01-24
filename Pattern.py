from turtle import*
import random
#
# speed(0)
# pensize(2)
# bgcolor('black')
#
# for i in range(102):
#     r=random.randint(0,255)
#     g=random.randint(0,255)
#     b=random.randint(0,255)
#     colormode(255)
#     pencolor(r,g,b)
#     for j in range(2):
#         fd(i)
#         rt(20)
#         lt(50)
#         rt(130)
#         fd(i)
#     rt(120)
# done()

# speed(0)
# bgcolor('black')
# pensize(4)
#
# for i in range(300):
#     r=random.randint(0,255)
#     g=random.randint(0,255)
#     b=random.randint(0,255)
#     colormode(255)
#     pencolor(r,g,b)
#     fd(i)
#     lt(59)
#
# done()

speed(5)
def rect(color):
    begin_fill()
    fillcolor(color)
    for i in range(2):
        fd(400)
        rt(90)
        fd(100)
        rt(90)
    end_fill()

screensize(1100,1100)
up()
pensize(10)
goto(0,-300)
down()
goto(0,400)
pensize(4)
rect("orange")
goto(0,300)
fd(200)
color("blue")
circle(-50)
setheading(270)
fd(50)
setheading(0)
for i in range (24):
    fd(45)
    bk(45)
    lt(15)
setheading(90)
fd(50)
setheading(0)
color("black")
fd(200)
rt(90)
fd(100)
rt(90)
goto(0,200)
rect("green")
rt(90)
fd(250)
lt(90)
penup()
fd(30)
pendown()
hideturtle()
color('blue')
write('Happy Republic Day of India',
      font=('arial',6,'normal'))

done()