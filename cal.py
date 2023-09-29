def cal(a,b,c):
    if c=='+':
        r=a+b
        print('sum is ',r)
    elif c=='-':
        r=a-b
        print('sub is ',r)
    elif c=='*':
        r=a*b
        print('multiplication is ',r)
    elif c=='/':
        r=a/b
        print('Division is ',r)
x=int(input("enter first number"))
y=int(input("enter second number"))
z=input("Enter Symbol")
cal(x,y,z)