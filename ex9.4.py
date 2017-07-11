name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
line = list()
addBook = dict()

for line in handle:
    if line.startswith('From '): 
#        line.split()
#        addBook = count(line[1]).get(line[1],0) + 1
        print(line.split())
    else: continue
        
