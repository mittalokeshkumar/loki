#Given the weekday of the first day of the month,Determine the day of the week of the given date in that month
a=input()
b=int(input())
if(a=="Monday"):
    if(b%7==0):
        print("Sunday")
    if(b%7==1):
        print("Monday")
    if(b%7==2):
        print("Tuesday")
    if(b%7==3):
        print("Wednesday")
    if(b%7==4):
        print("Thursday")
    if(b%7==5):
        print("Friday")
    if(b%7==6):
        print("Saturday")
elif(a=="Tuesday"):
    if(b%7==6):
        print("Sunday")
    if(b%7==0):
        print("Monday")
    if(b%7==1):
        print("Tuesday")
    if(b%7==2):
        print("Wednesday")
    if(b%7==3):
        print("Thursday")
    if(b%7==4):
        print("Friday")
    if(b%7==5):
        print("Saturday")
elif(a=="Wednesday"):
    if(b%7==5):
        print("Sunday")
    if(b%7==6):
        print("Monday")
    if(b%7==0):
        print("Tuesday")
    if(b%7==1):
        print("Wednesday")
    if(b%7==2):
        print("Thursday")
    if(b%7==3):
        print("Friday")
    if(b%7==4):
        print("Saturday")
elif(a=="Thursday"):
    if(b%7==4):
        print("Sunday")
    if(b%7==5):
        print("Monday")
    if(b%7==6):
        print("Tuesday")
    if(b%7==0):
        print("Wednesday")
    if(b%7==1):
        print("Thursday")
    if(b%7==2):
        print("Friday")
    if(b%7==3):
        print("Saturday")
elif(a=="Friday"):
    if(b%7==3):
        print("Sunday")
    if(b%7==4):
        print("Monday")
    if(b%7==5):
        print("Tuesday")
    if(b%7==6):
        print("Wednesday")
    if(b%7==0):
        print("Thursday")
    if(b%7==1):
        print("Friday")
    if(b%7==2):
        print("Saturday")
elif(a=="Saturday"):
    if(b%7==2):
        print("Sunday")
    if(b%7==3):
        print("Monday")
    if(b%7==4):
        print("Tuesday")
    if(b%7==5):
        print("Wednesday")
    if(b%7==6):
        print("Thursday")
    if(b%7==0):
        print("Friday")
    if(b%7==1):
        print("Saturday")
elif(a=="Sunday"):
    if(b%7==1):
        print("Sunday")
    if(b%7==2):
        print("Monday")
    if(b%7==3):
        print("Tuesday")
    if(b%7==4):
        print("Wednesday")
    if(b%7==5):
        print("Thursday")
    if(b%7==6):
        print("Friday")
    if(b%7==0):
        print("Saturday")
