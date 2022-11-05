n=int(input())
x1=int(input())
x2=int(input())
x3=int(input())
while x1>0 and x2>0 and x3>0 and x1+x2+x3==n:
    if x1!=x2 and x2!=x3 and x1!=x3:
        print("FAIR")
    else:
        print("UNFAIR")
    break