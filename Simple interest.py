def simpleinterest(p,t,r):
    print("Principal:",p)
    print("Time:",t)
    print("Rate of interest:",r)
    si=(p*t*r)/100
    print("The simple interest is",si)
    return si
p=float(input("Enter the principal amount:"))
t=float(input("Enter the time:"))
r=float(input("Enter the rate of interest:"))
simpleinterest(p,t,r)