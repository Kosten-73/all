import PyPDF2
import re

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

# Откройте файл в бинарном режиме
with open('resu4.pdf', 'rb') as file:
    reader = PyPDF2.PdfReader(file)
    k = 0
    mas = []
    # Пройти по всем страницам
    for page in reader.pages:
        text1 = re.split(r'09.04.04', page.extract_text())
        # print(text1)
        for now in text1:
            now1 = now.split()
            # print(now1)
            mas1 = []
            if len(now1) != 0:
                if now1[0] == 'Программная':
                    mas1.append(now1[0])
                    mas1.append(now1[1])
                    mas1.append(now1[2])
                    mas1.append(now1[3])
                    mas1.append(now1[4])
                    if now1[4] == 'Прищепа':
                        now1[5] = 90
                    mas1.append(now1[5])
                    # mas1.append(now1[6])
                    # mas1.append(now1[7])
                    if is_number(now1[5]):
                        mas.append(mas1)

                    # print(now1)
            #     if now1[0] == 'Программная' and now1[1] == 'инженерия':
            #         print(now1)
            #     if now1[0] = :
            #         mas.append(now1)
            #         print(now1)

print(mas)
sorted_array = sorted(mas, key=lambda x: -int(x[-1]))
n = 1

for now in sorted_array:
    print(n, now)
    n += 1
# программная инж '09.04.04'