largest = None
smallest = None
while True:
    num = input("Enter a number: ")

    if num == "done" :
        break
# excption handling
    try:
        fval = float(num)
    except:
        print('Invalid Input')
        continue
# update largest
    if largest == None:
        largest = fval
    elif fval > largest:
        largest = fval
# update smallest
    if smallest == None:
        smallest = fval
    elif fval < smallest:
        smallest = fval

print("Maximum is", largest)
print("Minimum is", smallest)
