a = 1.1

ans = "Uzytkownik wprowadzil "

if type(a) == str:
    ans += "string"
elif type(a) == int:
    ans += "int"
elif type(a) == float:
    ans += "float"
elif type(a) == bool:
    ans += "bool"

print(ans)