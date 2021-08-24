def computepay(h,r):
    if h <= 40:
        return h*r
    else:
        h1 = h-40
        return 40*r+h1*1.5*r

hrs = float(input("Enter Hours: "))
rph = float(input("Rate per hour: "))
p = computepay(hrs,rph)
print(p)
