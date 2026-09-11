s = "1" * 60 + "2" * 60 + "3" * 60
while "21" in s or "31" in s or "23" in s:
    if "21" in s:
        s = s.replace("21", "12", 1)
    if "31" in s:
        s = s.replace("31", "13", 1)
    if "23" in s:
        s = s.replace("23", "32", 1)
print(s[12], s[112], s[172])
