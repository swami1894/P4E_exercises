name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
lst = list()
maillst=dict()
count = None
most = None

for line in handle:
    if line.rstrip().startswith('From '):
        try:
            lst.append(line.rstrip().split()[5][:2])
        except:
            lst[0] = line.rstrip().split()[5][:2]
    else:
        continue

for time in lst:
    maillst[time] = maillst.get(time,0) + 1

maillst = sorted([(time,freq) for (time,freq) in maillst.items()])

for (time,freq) in maillst:
    print(time, freq)
