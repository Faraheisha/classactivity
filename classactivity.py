def checking(num):
    if num%2==0:
        s=0
        return s
    else:
        s=1
        return s

num=int(input("enter a number :"))
result=checking(num)
if result==0:
    print(num," is even  number.")
else:
    print(num," is odd number.")


