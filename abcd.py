# Python Program to Calculate Sum of Odd Numbers from 1 to 100

minimum = int(input(" Please Enter the startingpoint : "))
maximum = int(input(" Please Enter the end point : "))
Oddtotal = 0

for number in range(minimum, maximum+1):
    if(number % 2 != 0):
        print("{0}".format(number))
        Oddtotal = Oddtotal + number

print("The Sum of Odd Numbers from {0} to {1} = {2}".format(minimum, maximum, Oddtotal))