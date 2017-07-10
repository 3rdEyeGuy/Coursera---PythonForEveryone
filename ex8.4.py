fname = input("Enter file name: ")
fh = open(fname)
lst = list()
mstrLst = list()

for line in fh:
    lst = line.split()
    lstRng = range(len(lst))
    for tempWrd in lst:
        if not tempWrd in mstrLst: mstrLst.append(tempWrd)

msrtSrt = mstrLst.sort()
print(mstrLst)

