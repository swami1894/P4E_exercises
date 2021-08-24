fname = input("Enter file name: ")

try:
	fh = open(fname)
except:
    print("file not found")
    quit()

for i in fh:
	print(i.rstrip().upper())
