FileName = input("Enter the input file name: ")
file = open(FileName, 'r')
NumLine = 0
for line in file:
    NumLine = NumLine + 1
print("The file has",NumLine,"lines.")
while True:
    linenum = 0
    num = int(input("Enter a line number [0 to quit]: "))
    if num >=1 and num <= NumLine:
        file = open(FileName, 'r')
        for lines in file:
            linenum = linenum + 1
            if linenum == num:
                print(num,":",lines)
    elif num == 0:
        break
    else:
        if num!= NumLine:
            print("ERROR: Please enter a line number that is less than",NumLine)
