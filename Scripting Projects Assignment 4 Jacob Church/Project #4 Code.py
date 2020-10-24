height = float(input("Please enter an initial height to drop the ball from:"))
bounces = int(input("Please enter an amount of times the ball will bounce:"))
bounciness = 0.6
distance = 0
while bounces > 0:
    distance = distance + height
    height = height * bounciness
    distance = distance + height
    bounces -= 1
    print("Total distance traveled is ", distance)
