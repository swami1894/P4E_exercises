import re

name = input("Enter file:")
if len(name) < 1 : name = "assignregx.txt"
handle = open(name)
total = 0     #Sum of list of numbers in each line

lst=list()     # save each line from the file
lst_nums = list()  # save the numbers in each line as a list

# save each line in list
for line in handle:
    try:
        lst.append(line.rstrip())
    except:
        lst[0] = line.rstrip()

# below to extract number from each line
for statemen in lst:
    try:
        lst_nums.append(re.findall('[0-9]+', statemen))
    except:
        lst_nums[0] = re.findall('[0-9]+', statemen)

# Check if the list is empty or not if not find sum of each list and add it
#sum of complete list of list of numbers
for lst_num in lst_nums:
    if len(lst_num) > 0:
        for num in lst_num:
            total =  total + int(num)

print(total)
