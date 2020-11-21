#Jacob Church
#Fall 2020
#11-07-2020
#Professor Ken Dewey
#importing turtle graphics
import turtle
#creating function of drawCircle
def drawCircle (centerpoint, radius):
    """This function draws a circle by using the given coordinates"""
    (x,y) = centerpoint
    turtle.up()
    turtle.setpos(x,y)
    turtle.down()
    turtle.circle(radius)
    #making the print statements for the calculations of circumference
    print("The radius of the circle is", radius)
    print("The circumference of the circle is", (2.0 * 3.14 * radius))
#giving the coordinates for the x, y, and radius
drawCircle((20, 20), 20)
