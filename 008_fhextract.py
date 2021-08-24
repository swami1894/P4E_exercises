# Use the file name mbox-short.txt as the file name
import decimal

fname = input("Enter file name: ")
fh = open(fname)
count = 0
sum  = 0.0
average= 0.0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    count = count + 1
    pos = line.find(':')
    xnum = line[pos+1:]
    tnum = xnum.strip()
    fnum = float(tnum)
    sum = sum + fnum

avg = decimal.Decimal(sum/count)
print("Average spam confidence: ", round(avg,12))
