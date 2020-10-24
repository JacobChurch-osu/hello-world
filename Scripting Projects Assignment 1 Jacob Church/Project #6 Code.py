Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:43:08) [MSC v.1926 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> radius = int(input("Enter the radius: "))
Enter the radius: 7
>>> area = 3.14 * radius ** 2
>>> print("The area is", area, "square units.")
The area is 153.86 square units.
>>> radius = int(input("Enter the radius: "))
Enter the radius: 6.31
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    radius = int(input("Enter the radius: "))
ValueError: invalid literal for int() with base 10: '6.31'
>>> radius = float(input("Enter the radius: "))
Enter the radius: 6.31
>>> area = 3.14 * radius ** 2
>>> print("The area is", area, "square units.")
The area is 125.02255399999999 square units.
>>> radius = float(input("Enter the radius: "))
Enter the radius: 14.96
>>> print("The area is", area, "square units.")
The area is 125.02255399999999 square units.
>>> radius = float(input("Enter the radius: "))
Enter the radius: 14.96
>>> area = 3.14 * radius ** 2
>>> print("The area is", area, "square units.")
The area is 702.7370240000001 square units.
>>> 