name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
lin = list()
dic = dict()
dicLs = list()

for lin in handle:
    if lin.startswith('From '):
        words = lin.split()
        tim = words[5].split(':')
        hr = str(tim[0])
        dic[hr] = dic.get(hr,0) + 1
        dicLs = dic.items()
    else: continue
hrSort = sorted([(k,v) for k,v in dicLs])

print(hrSort)       
