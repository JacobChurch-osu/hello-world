numbers = []
print("Press the enter key to stop")
while(True):
    num = input("Please enter a number:")
    if num:
        numbers.append(float(num))
    elif(num == ''):
            break
sumNum =0
for num in numbers:
    sumNum += num
avg = sumNum / len(numbers)
print("The sum of your integers is ",sumNum)
print("The average of your numbers is ",avg)
