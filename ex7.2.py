# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
value = 0
count = 0

for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    cLine = line.rstrip()
    valIndex = cLine.find(":")
    value = float(cLine[valIndex+2:valIndex+8]) + value
    count = count + 1

avgConf = value/count
print("Average spam confidence:", avgConf)

