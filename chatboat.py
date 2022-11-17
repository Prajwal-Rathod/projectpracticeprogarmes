
# disigning a simple chatbot using if else statment
print("hello,i am chatboat")
print("how may i help you")
print("hit 1 for software instalation request")
print("hit 2 for software update request ")
print("hit 3 for software uninstall request")
print("hit 4 for software repaire request")
print("hit 5 for other request")

# accepting the user request
userinput=int(input("enter your choice"))
# using if else statment to  procces the request
if userinput==1:
    softwareneeded=input("please provide the sotwear name")
elif userinput==2:
    softwareupdate=input("please provide the softwaere name and name to be updated")
elif userinput==3:
    softwareuninstall=input("please provide the name of the software to be uninstalled")
elif userinput==4:
    softwarerepair=input("please provide the software name to be repaired")
else:
    OtherRequests=input("please provide the details of your request")
    print("thankyou for using the service")


