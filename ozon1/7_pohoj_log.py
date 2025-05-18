def algo(stri, masiv):
    if stri in masiv:
        return 1
    if stri[-1] + stri[1:] + stri[0] in masiv:
        return 1
    for j in range(1, len(stri) - 1):
        variant1 = stri[:j - 1] + stri[j] + stri[j - 1] + stri[j + 1:]
        variant2 = stri[:j] + stri[j + 1] + stri[j] + stri[j + 2:]

        if variant1 in masiv or variant2 in masiv:
            return 1

    return 0


mas = list()
for _ in range(int(input())):
    mas.append(input())
for _ in range(int(input())):
    print(algo(input().strip(), mas))
