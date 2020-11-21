#Jacob Church
#Fall 2020
#11-07-2020
#Professor Ken Dewey
#creating the def statement
def isSorted(lyst):
    #creating the for statement and meat of the program
    for i in range(1,len(lyst)):
        if lyst[i - 1] > lyst[i]:
            return False
    return True
#initializing the argumented list
List = [2, 4, 5, 8, 13]
#printing the sorted or not sorted result
print("The List involved in the argument is: ", List)
print("If the list is sorted, it will be True, and if it is not sorted, it will be False.")
print("The List is", isSorted(List))
