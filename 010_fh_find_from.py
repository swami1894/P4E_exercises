fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"

fh = open(fname)
count = 0

for line in fh:
    if line.rstrip().startswith('From:'):
        print(line.rstrip().split()[1])
        count = count + 1
    else:
        continue

print("There were", count, "lines in the file with From as the first word")
