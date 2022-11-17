import time
#time input
min=int(input("enter the menutes: "))
sec= int(input("enter the seconds: "))

#we are checking for valid seconed input
if(sec>60):
    print("seconds cannot be more than 60")
    sec=0
    min+=1

#converting menuts into seconds
sec=min*60+sec
s=0

#running loop for every second
for i in range(sec):
    m=int(i/60)
    s=s+1
    if(s>=60):
        m=m+1
        s=0
    print(f"{m} menuts,{s} seconds")
    time.sleep(1)

print("your time is up ")
