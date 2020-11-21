def newtonSquare(x):
    def f(x, estimate):
        if abs(x-estimate ** 2) <= 0.000001:
            return estimate
        else:
            return f(x, (estimate + x / estimate) / 2)
    return f(x, 1.0)
def main():
    num = int(input('Enter a positive number to receive the square root:'))
    print ("The square root of",num,"is", newtonSquare(num))
main()
