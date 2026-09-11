from itertools import*
schetckik = 0
for number, word in enumerate(product(sorted("ИНФОРМАТ"), repeat=5), start=1):
    if number %2 != 0 and word[0] != "О" and 1<= word.count("Н") <= 2:
        print(number,word)
        schetckik += 1

print(schetckik)

