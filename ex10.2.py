name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
lin = list()
dic = dict()

for lin in handle:
    if lin.startswith('From '):
        words = lin.split()
#        print(words)
        tim = words[5].split(':')
        hr = str(tim[0])
#        print(hr)
        dic[hr] = dic.get(hr,0) + 1
    else: continue

print(dic)
        
