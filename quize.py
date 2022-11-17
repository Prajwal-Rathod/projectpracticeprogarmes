#quize applicxation
#for student details
name=input("enter the student name")
USN=input("enter the usn")
score=0
# qutions 1
print("objective type qutions\n please choice the correct answer for each qution")
print("the battle of plassy was fought in ")
print("choice")
print("option.1=1757")
print("option.2=1782")
print("option.3=1748")
print("option.3=1764")
answer=int(input("enter the right option\n"))
if (answer==1):
    print("your answer is correct\n")
    score=score+1
    print("your score is",score)

else:
    print("answer is wrong")
    print("Your score is",score)


# qutions 2
print("The territory of Porus who offered strong resistance to Alexander was situated between the rivers of")
# for pri nting the option and entering the option
print("choice")
print("option.1=Sutlej and Beas")
print("option.2=Jhelum and Chenab")
print("option.3=Ravi and Chenab")
print("option.3=Ganga and Yamuna")
answer=int(input("enter the right option\n"))
if (answer==2):
    print("your answer is right\n")
    score=score+1
    print("your score is",score)
else:
    print("your answre is wrong\n")
    print("your score is",score)
# qutions 3
# for pri nting the option and entering the option
print("Under Akbar, the Mir Bakshi was required to look after")
print("choice")
print("option.1=military affairs")
print("option.2=the state treasury")
print("option.3the royal household")
print("option.4=the land revenue system")
answer=int(input("enter the right option\n"))

if (answer==1):
    print("your anser is correct\n")
    score=score+1
    print("your score is ",score)
else:
    print("your answer is wrong\n")
    print("your score is",score)

# for pri nting the option and entering the option
# qutions 4
print("Tripitakas are sacred books of")
print("choice")
print("option.1=Buddhists")
print("option.2=Hindus")
print("option.3=Jains")
print("option.4=None of the above")
answer=int(input("enter the right option\n"))
if (answer==3):
    print("your anser is correct\n")
    score=score+1
    print("your score is",score)
else:
    print("your answer is wrong\n")
    print("your score is ",score)


# for pri nting the option and entering the option
# qutions 4
print("The trident-shaped symbol of Buddhism does not represent")
print("Tripitakas are sacred books of")
print("choice")
print("option.1=bhudda")
print("option.2=sankha")
print("option.3=nirvahana")
print("option.4=dhamma")
answer=int(input("enter the right option\n"))
if (answer==4):
    print("your anser is correct\n")
    score=score+1
    print("your score is",score)
else:
    print("your answer is wrong\n")
    print("your score is ",score)

#to end the quize
print("thank you")
print(name)
print(USN)
print("your total score is",score)
print("department of history")