Python 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 03:13:28) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> import turtle
>>> myt = turtle.Turtle()
>>> scr = turtle.Screen()
>>> scr.delay()
10
>>> scr.delay(0)
>>> scr.delay()
0
>>> myt.speed()
3
>>> myt.speed(0)
>>> myt.speed()
0
>>> myt.hideturtle()
>>> myt.penup()
>>> myt.goto(40,40)
>>> myt.pendown()
>>> myt.circle(100)
>>> myt.fillcolor("red")
>>> myt.begin_fill()
>>> myt.circle(100)
>>> myt.end_fill()
>>> myt.penup()
>>> myt.goto(-50,-50)
>>> myt.pendown()
>>> myt.fillcolor("blue")
>>> myt.begin_fill()
>>> for i in range(4):
	myt.forward(100)
	myt.right(90)

	
>>> myt.end_fill()
>>> # CSCI 1133, Lab Section 013, lab13 Jeffery Liu, Warm-up
