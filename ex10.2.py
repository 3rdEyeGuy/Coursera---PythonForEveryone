name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
lin = list()

for lin in handle:
    if lin.startswith('From '):
        words = lin.split()
#        print(words)
        tim = words[5]
        hr = tim.split(':')
        print(hr)

