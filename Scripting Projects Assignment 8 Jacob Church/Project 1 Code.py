import math
Toler = 0.000001
def newton(x):
   """ Returns the square root of UserNum """
   Estimate = 1.0
   while True:
       Estimate = (Estimate + x / Estimate) / 2
       Diff = abs(x - Estimate ** 2)
       if Diff <= Toler:
           break     
       return Estimate
def main():
   """Allows the user to obtain square roots."""
   while True:
       x = input("Enter a positive number or press enter to quit: ")
       if x == "":
           break
       x = float(x)
       print("The programs estimate of the square root of ", x, "is ", round(newton(x),2))
       print("Python's estimate: ", math.sqrt(x))
main()
