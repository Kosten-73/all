s = "2" + "5" * 103
while "25" in s or "2" in s:
    if "25" in s:
        s = s.replace("25", "552", 1)
    else:
        s = s.replace("2", "555", 1)
print(s.count("5"))
