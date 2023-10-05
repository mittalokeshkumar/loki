#printing my name with help of the python. 
n=int(input())
#L
for i in range(1,n+1):
    if(i==n):
        print("L "*n)
    else:
        print("L ")
#O
for i in range(1,n+1):
    if(i==1) or (i==n):
        print("O "*n)
    else:
        print("O "+"  "*(n-2)+"O ")
#K
a=int((n/2)+1)
for i in range(1,n+1):
    if(i==1) or (i==n):
        print("K "+"  "*(n-2)+"K ")
    elif(i>1) and (i<a):
        print("K "+"  "*(n-i-1)+"K ")
    elif(i==a):  
        print("K "+"  "*(n-a-1)+"K ")
    elif(i>a) and (i<n):
        print("K "+"  "*(i-2)+"K ")
#I
b=int(n/2)
for i in range(1,n+1):
    if(i==1) or (i==n):
        print("I "*n)
    else:
        print("  "*b+"I ")
