#In this program, we will allow users to input l,side,factor to draw polygons outward.
#polygon() function I defined basically determines what types of polygons we will be drawing.
#get_me_poly() function has a for-loop that iterate the vaule from 10 - 80. Notices that we need
#to adjust steps within our for-loop bc without adjustment we get equal shrinks between each polygon.
#so we need to twist by define a function powerloop() which employs a while loop to let step parameters*2
#That is, when we call get_me_the_poly, we iterate starting from 10 with multiplying the shrinks we expand by 2.
#We get what we expect.
import turtle 
l = int(input("Enter the length of the sides of the polygon : "))
sides = int(input("Enter the number of sides of the polygon:"))
factor = int(input("Enter the sfactor of polygon that expand outward:")) 
def polygon(sides,l):
    for x in range(sides):
        turtle.forward(l)
        turtle.left(360/sides)
def powerloop(mn,mx,step):
    while mn < mx:
        yield mn
        mn *= step
def get_me_the_poly(factor):
    s = turtle.Screen()
    t = turtle.Turtle()
    for i in powerloop(10,100,factor):
        polygon(sides,i)
        t.up()
        t.down()    
    s.exitonclick()
get_me_the_poly(factor)