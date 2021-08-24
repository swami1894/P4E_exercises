# Calculate gross pay for 40 hrs or more

hrs = float(input("Enter hours: "))
ratePerHrs = float(input("Enter rate per hour: "))

if hrs <= 40:
  grossPay = hrs*ratePerHrs
else:
  extraHrs = hrs - 40
  grossPay = (40*ratePerHrs) + (1.5*extraHrs*ratePerHrs)

print(grossPay)
