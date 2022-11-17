# finding the sum og first n whole numbers using loop
endpoint=int(input("enter the value of n:"))
sum_of_numbers=0
for i in range(endpoint):
    print("sum of numbers value is:",sum_of_numbers)
    print("index value is:",i)
    sum_of_numbers=sum_of_numbers+i
print("the sum of first {} whole numbers is {}".format(endpoint,sum_of_numbers))
#finding the sum of numbers between a givan range (start point to end point)
start_point=int(input("enter the start point"))
endpoint=int(input("enter the endpoint:"))
sum_of_numbers=0
step=1,2
for i in range(start_point,endpoin0t,step):
        sum_of_numbers=sum_of_numbers+i
        print("the sum of odd numbers between {} and {} is{}".format(start_point,endpoint,sum_of_numbers))