hrs = input("Enter Hours:")
h = float(hrs)
rate = input("Enter rate:")
if h > 40:
    overT = h - 40
    overP = overT * float(rate) * 1.5
    pay= 40 * float(rate) + overP
elif h <= 40:
    pay = h * float(rate)
print(pay)
