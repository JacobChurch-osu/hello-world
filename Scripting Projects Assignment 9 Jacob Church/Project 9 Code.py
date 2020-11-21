#Jacob Church
#Fall 2020
#11-07-2020
#Professor Ken Dewey
#opening the file.
import functools
file = open("numbers.txt", 'r')
file = file.read()
#turning the file into a list with split command.
file = file.split()
#turning the file into integers with map command.
file = list(map(int, file))
#using lambda function to create the average of the file.
print("The average number of the given file is: ",functools.reduce(lambda x, y: x+y / len(file), file, 0))
