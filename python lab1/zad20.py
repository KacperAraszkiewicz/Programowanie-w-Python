a = 1
b = 8
c = 1

delta = b**2 - 4*a*c

if delta < 0:
    print("brak miejsc zerowych")
elif delta == 0:
    mz = -b/2*a
    print(mz)
elif delta > 0:
    mz1 = (-b - delta)/2*a
    mz2 = (-b + delta)/2*a
    print(mz1, mz2)