# to and the plane whwn it is at an altitude of 5k
#taking input from the pilot
print("hello i am your pilot")
print("can u please inform me on what altitude u are ")
print("please enter the altitude \n")
altitude = int(input())
if (altitude >= 10000 ):
    print("copy that, please go around ")
elif (altitude <= 5000 ):
    print("copy that, can u please land the plane ")
elif (altitude >= 5000):
    print("go around ")
else:
    print("invalid input")