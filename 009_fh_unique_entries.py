fname = input("Enter file name: ")
fh = open(fname)
lst = list()

for line in fh:
    for word in line.rstrip().split():
        try:
            if word not in lst:
                lst.append(word)
            else:
                continue
        except:
            lst[0]=word

lst.sort()
print(lst)
