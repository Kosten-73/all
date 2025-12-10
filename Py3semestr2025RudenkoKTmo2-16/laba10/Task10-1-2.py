from scipy import stats
import pandas as pd
import numpy as np

np.random.seed(42)

data_A = np.random.normal(loc=5.0, scale=1.0, size=50)

data_B = np.random.normal(loc=4.2, scale=1.0, size=50)

df = pd.DataFrame({"A": data_A, "B": data_B})
df.to_csv("Время_загрузки.csv", index=False)
print(df.head(50))

df = pd.read_csv("Время_загрузки.csv")

A = df["A"]
B = df["B"]

# Средние и стандартное отклонение
mean_A, mean_B = A.mean(), B.mean()
std_A, std_B = A.std(ddof=1), B.std(ddof=1)
n_A, n_B = len(A), len(B)


# Функция для доверительного интервала
def confidence_interval(data, confidence=0.95):
    mean = data.mean()
    sem = stats.sem(data)  # стандартная ошибка среднего
    h = sem * stats.t.ppf((1 + confidence) / 2., len(data) - 1)
    return mean - h, mean + h


ci_95_A = confidence_interval(A, 0.95)
ci_95_B = confidence_interval(B, 0.95)
ci_99_A = confidence_interval(A, 0.99)
ci_99_B = confidence_interval(B, 0.99)

print("95% CI A:", ci_95_A)
print("95% CI B:", ci_95_B)
print("99% CI A:", ci_99_A)
print("99% CI B:", ci_99_B)

# T-тест
t_stat, p_value = stats.ttest_ind(A, B)
print("t-statistic:", t_stat)
print("p-value:", p_value)

alpha = 0.05
if p_value < alpha:
    print("Разница статистически значима на уровне 0.05")
else:
    print("Разница НЕ статистически значима на уровне 0.05")

# C:\Users\korudenko\AppData\Local\Programs\Python\Python312\python.exe C:\Users\korudenko\PycharmProjects\Py3semestr2025RudenkoKTmo2-16\laba10\Task10-1-2.py
#            A         B
# 0   5.496714  4.524084
# 1   4.861736  3.814918
# 2   5.647689  3.523078
# 3   6.523030  4.811676
# 4   4.765847  5.231000
# 5   4.765863  5.131280
# 6   6.579213  3.360782
# 7   5.767435  3.890788
# 8   4.530526  4.531263
# 9   5.542560  5.175545
# 10  4.536582  3.720826
# 11  4.534270  4.014341
# 12  5.241962  3.093665
# 13  3.086720  3.003793
# 14  3.275082  5.012526
# 15  4.437712  5.556240
# 16  3.987169  4.127990
# 17  5.314247  5.203533
# 18  4.091976  4.561636
# 19  3.587696  3.554880
# 20  6.465649  4.561396
# 21  4.774224  5.738037
# 22  5.067528  4.164174
# 23  3.575252  5.764644
# 24  4.455617  1.580255
# 25  5.110923  5.021903
# 26  3.849006  4.287047
# 27  5.375698  3.900993
# 28  4.399361  4.291761
# 29  4.708306  2.212431
# 30  4.398293  3.980328
# 31  6.852278  4.557113
# 32  4.986503  5.677894
# 33  3.942289  3.681730
# 34  5.822545  3.391506
# 35  3.779156  3.698243
# 36  5.208864  5.115402
# 37  3.040330  4.528751
# 38  3.671814  3.670240
# 39  5.196861  4.713267
# 40  5.738467  4.297078
# 41  5.171368  5.168645
# 42  4.884352  3.497947
# 43  4.698896  3.872338
# 44  3.521478  3.807892
# 45  4.280156  2.736485
# 46  4.539361  4.496120
# 47  6.057122  4.461055
# 48  5.343618  4.205113
# 49  3.236960  3.965413
# 95% CI A: (np.float64(4.509180362858151), np.float64(5.039871826629568))
# 95% CI B: (np.float64(3.969300458345402), np.float64(4.466261282590504))
# 99% CI A: (np.float64(4.4206633456797), np.float64(5.128388843808019))
# 99% CI B: (np.float64(3.8864095644461396), np.float64(4.549152176489766))
# t-statistic: 3.077696235005867
# p-value: 0.0027052721035458497
# Разница статистически значима на уровне 0.05
#
# Process finished with exit code 0
