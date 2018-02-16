from turtle import*
import time
from random import randint

right(90)
penup()
goto(-200,200)
pendown()



for i in range(1,15):
 write(i)
 for j in range(11):
  fd(10)
  penup()
  fd(10)
  pendown()
 
 penup()
 goto(-200+(30*i),200)
 pendown()

 

t1=Turtle()
t1.color("red")
t1.shape('turtle')
t1.penup()
t1.goto(-230,170)
t1.pendown()
t1.right(360)

t2=Turtle()
t2.color("blue")
t2.shape('turtle')
t2.penup()
t2.goto(-230,120)
t2.pendown()
t2.right(360)

t3=Turtle()
t3.color("yellow")
t3.shape('turtle')
t3.penup()
t3.goto(-230,70)
t3.pendown()
t3.right(360)

t4=Turtle()
t4.color("green")
t4.shape('turtle')
t4.penup()
t4.goto(-230,20)
t4.pendown()
t4.right(360)

for step in range(120):
 t1.fd(randint(1,6))
 t2.fd(randint(1,6))
 t3.fd(randint(1,6))
 t4.fd(randint(1,6))
 

time.sleep(5)

