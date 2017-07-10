# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)

fR = fh.read()
fR = fR.rstrip()
value = 0

for line in fR:
    if not line.startswith("X-DSPAM-Confidence:") : continue 
#index = line.find("0")
print(line)
#print(index)
#value = float(line[index:index+6]) + value

#print(value)

#    print(line.rstrip())
print("Done")

