def computepay(h,r):
    if h > 40:
        overT = h-40
        pay = overT * r * 1.5 + (40 * r)
    elif h <= 40:
        pay = h * r
    return pay 

hrs = input('Enter Hours: ')
rate = input('Enter rate: ')

try:
    p = computepay(float(hrs),float(rate))
except:
    print('Input not of correct type!')
    quit()
print(p)
