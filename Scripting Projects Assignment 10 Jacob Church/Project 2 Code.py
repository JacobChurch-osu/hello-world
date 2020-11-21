#Jacob Church
#Fall 2020
#11-14-2020
#Prof. Ken Dewey
#importing the turtle graphics shell
from turtle import Turtle, tracer, update
#creating the funtion cCurve
def cCurve(t, x1, y1, x2, y2, level):
   #creating the function drawLine
   def drawLine(x1, y1, x2, y2):
      """Draws a line segment between the endpoints."""
      t.up()
      t.goto(x1, y1)
      t.down()
      t.goto(x2, y2)
   if level == 0:
      drawLine(x1, y1, x2, y2)
   else:
      xm = (x1 + x2 + y1 - y2) // 2
      ym = (x2 + y1 + y2 - x1) // 2
      cCurve(t, x1, y1, xm, ym, level - 1)
      cCurve(t, xm, ym, x2, y2, level - 1)
#creating the funtion main
def main():
   level = int(input("Enter the level (0 or greater): "))
   t = Turtle()
   if level > 8:
      tracer(False)
   #importing random module for color selection
   import random
   color = ["red", "blue", "green"]
   t.pencolor(random.choice(color))
   t.speed(0)
   t.hideturtle()
   cCurve(t, 50, -50, 50, 50, level)
   if level > 8:
      update()
if __name__ == "__main__":
   main()
