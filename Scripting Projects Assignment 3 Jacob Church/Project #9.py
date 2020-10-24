kilometers = float(input("Enter a distance in Kilometers: "))
degreesperMin = 90 * 60
oneKilo = degreesperMin/10000
Nautical = (oneKilo * kilometers)
print(kilometers, "is equal to", Nautical, "Nautical mile(s)")

