from turtle import *
import time

def koch(a, order):
    if order == 0:
        forward(a)
    else:
        koch(a/3, order-1)
        left(60)
        koch(a/3, order-1)
        right(120)
        koch(a/3, order-1)
        left(60)
        koch(a/3, order-1)

#setup
penup()
goto(-150, 0)
pendown()

koch(300, 5)
done()