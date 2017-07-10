# Use words.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
fhRead = fh.read()
fhUp = fhRead.upper()
print(fhUp.rstrip())

