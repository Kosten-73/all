s = "3" * 9 + "2" * 22
while "333" in s or "222" in s:
    while "333" in s:
        s = s.replace("333", "2", 1)
    while "222" in s:
        s = s.replace("222", "3", 1)
print(s)
