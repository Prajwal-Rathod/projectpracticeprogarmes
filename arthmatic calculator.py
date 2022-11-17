#python program to perform simple arhmatic calculation
# to perform simple simple arthmatic equations
num1=int(input("enter the first number :"))
num2=int(input("enter the sceond  number  :"))
print("enter which ofperation do u want to perfrom?:")
ch=input("use any of thise operators to spacific operation '+','-','*','/':")
result = 0
if ch == '+':
    result= num1+num2
elif ch == '-':
    result = num1-num2
elif ch == '*':
    result = num1*num2
elif ch == '/':
    result = num1/num2
else:
    print("input charecter is not recoginzed:")
print(num1,ch,num2,':',result)