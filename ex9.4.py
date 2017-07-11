name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
line = list()
addBook = dict()
max = None

for line in handle:
    if line.startswith('From '): 
        allWords = line.split()
        words = allWords[1]
        addBook[words] = addBook.get(words,0) + 1
    else: continue
for k,v in addBook.items():
    if max is None or v > max:
        max = v
        maxWord = k
print(maxWord, max)
