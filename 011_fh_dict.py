name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
lst = list()
maillst=dict()
count = None
most = None

for line in handle:
    if line.rstrip().startswith('From:'):
        try:
            lst.append(line.rstrip().split()[1])
        except:
            lst[0] = line.rstrip().split()[1]
    else:
        continue

for email in lst:
    maillst[email] = maillst.get(email,0) + 1

for email,num in maillst.items():
    if count == None or num > count:
        most = email
        count = num

print(most, count)
