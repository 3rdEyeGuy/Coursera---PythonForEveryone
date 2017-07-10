# Use words.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
for ln in fh:
    lstr = ln.rstrip()
    print(lstr.upper())
