iterations = int(input("Please enter a value for the amount of iterations for the method:"))
total=0
for i in range(1,iterations):
    total += (-1)**(i+1)*((1.0/(i+i+1)))

totalValue = 4*(1-total)
print(totalValue)
