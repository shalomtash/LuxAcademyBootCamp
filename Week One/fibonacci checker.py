#program that prints if a number is a fibonacci sequence or not


n=int(input("Enter the number: "))
c=0
a=1
b=1
if n==0 or n==1:
    print("is a fibonacci")
else:

    while c<n:
        c=a+b
        b=a
        a=c

    if c==n :

       print("is a fibonacci")

    else :

       print( "is not a fibonacci")