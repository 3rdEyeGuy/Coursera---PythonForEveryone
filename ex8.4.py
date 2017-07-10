fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    lst = line.split()
    print(lst[2])
