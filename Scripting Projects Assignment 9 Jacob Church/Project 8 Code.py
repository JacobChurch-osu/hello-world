#Jacob Church
#Fall 2020
#11-07-2020
#Professor Ken Dewey
#creating the def statement for printAll
def printAll(seq):
    if seq:
        #printing the initial element
        print(seq[0])
        #sending the function from element to element
        printAll(seq[1:])
#using the function to print the string, tuple, and list for the program
printAll("Hope This Works")
printAll((1,3,5,7))
printAll([2,4,6,8])
