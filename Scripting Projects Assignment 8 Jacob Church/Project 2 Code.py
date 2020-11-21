import math
def newton(x, Estimate):
    if abs (x-Estimate ** 2) <= 0.000001:
            return Estimate
    else:
        Estimate = newton(x, (Estimate + x/Estimate)/2)
    return Estimate                      
def main():
    while True:
        x = (input('Enter a positive number or enter/return key to quit: '))
        if x == "":    
                break
        x = float(x)
        print("Newtons estimate of the sqaure root of ", x, "is: ", newton(x, x/2))
        print("The True value of the square root is: ", math.sqrt(x))
main()
