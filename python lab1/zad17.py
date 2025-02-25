x = 1
y = 2
z = 3
bigger = 0
biggest = 0

if x > y:
    bigger = x
else:
    bigger = y

if bigger > z:
    biggest = bigger
else:
    biggest = z

print(biggest)