#accept 3 marks from the user and print the avarage of best of 2
marks1=int(input("enter the marks1:"))
marks2=int(input("enter the marks2"))
marks3=int(input("enter the marks 3:"))
if marks1<marks2 and marks1<marks3:
    print("avarage of best of two marks:",(marks2+marks3)/2)
elif marks2<marks3 and marks<marks1:
    print("avarage of best of 2 marks:",(marks3+marks1)/2)


