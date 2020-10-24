name = input("Enter the file name: ")
readFile = open(name,"r")
fileContent = readFile.readlines()
print("\nName\t\t\tHours\t\tTotal Pay");
for eachLine in fileContent:
    splitContent = eachLine.split(" ")
    hourlyWage = str(splitContent[1])
    hoursworked = str(splitContent[2])
    totalPay = hourlyWage * hoursworked
    print("{0:14}\t\t{1:>5}\t\t{2:>9}".format(splitContent[0],splitContent[1],totalPay));
readFile.close()
