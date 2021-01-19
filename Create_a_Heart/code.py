---
#Project Name -> Create a heart with TURTLE
#Author -> Priya Mondal
---

#What is TURTLE? -> Turtle graphics is a popular way for introducing programming to kids.
#It was part of the original Logo programming language developed by Wally Feurzeig, Seymour Papert and Cynthia Solomon in 1967
import turtle 
#Define properties
turtle.speed(1)   #The SPEED method creates ANIMATIONS, at certain speed.
turtle.bgcolor('pink')  #Set the background color as your choice. Deafult bgcolor -> White.
turtle.pensize(10)   

def func():
    for i in range(200):
     turtle.right(1)
     turtle.forward(1)

turtle.color('white', 'red')
turtle.begin_fill()

turtle.left(140)
turtle.forward(111.65)

#Calling the Function
func()

#changing the mouse direction
turtle.left(120)

#To finish the other part, calling the function
func()
turtle.forward(111.65)
turtle.end_fill()
turtle.hideturtle()

#To hold the screen
turtle.done()
