s = ">" + "6" * 29 + "4" * 16 + "3" * 13
while ">6" in s or ">4" in s or ">3" in s:
    # if ">6" in s:
    #     s = s.replace(">6", "44>", 1)
    # if ">4" in s:
    #     s = s.replace(">4", "4>", 1)
    # if ">3" in s:
    #     s = s.replace(">3", "6>", 1)
    s = s.replace(">6", "44>", 1) if ">6" in s else s
    s = s.replace(">4", "4>", 1) if ">4" in s else s
    s = s.replace(">3", "6>", 1) if ">3" in s else s
print(s)
print(s.count("4") * 4 + s.count("6") * 6)
print(sum(map(int, s[:-1])))
print(sum([int(digit) for digit in s[:-1]]))
