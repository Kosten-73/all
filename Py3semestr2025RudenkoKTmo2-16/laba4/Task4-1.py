import random


class Deposit:
    def __init__(self, amount, rate, period):
        self.amount = amount
        self.rate = rate
        self.period = period

    def calculate_profit(self):
        raise NotImplementedError("Нужно реализовать в подклассе")

class FixedDeposit(Deposit):
    def calculate_profit(self):
        return self.amount * self.rate * self.period

class BonusDeposit(Deposit):
    def __init__(self, amount, rate, period, bonus_threshold, bonus_rate):
        super().__init__(amount, rate, period)
        self.bonus_threshold = bonus_threshold
        self.bonus_rate = bonus_rate

    def calculate_profit(self):
        profit = self.amount * self.rate * self.period
        if self.amount >= self.bonus_threshold:
            profit += profit * self.bonus_rate
            print("Бонус!")
        return profit

class CompoundDeposit(Deposit):
    def calculate_profit(self):
        return self.amount * ((1 + self.rate) ** self.period - 1)

# Фабрика вкладов
class DepositFactory:
    @staticmethod
    def create_deposit(deposit_type, **kwargs):
        if deposit_type == "Срочный вклад":
            return FixedDeposit(**kwargs)
        elif deposit_type == "Бонусный вклад":
            return BonusDeposit(**kwargs)
        elif deposit_type == "Вклад со сложным процентом":
            return CompoundDeposit(**kwargs)
        else:
            raise ValueError("Неизвестный тип вклада")


# --- Пример использования ---
if __name__ == "__main__":
    for i in range(10):
        a = random.randint(5000, 100000)  # сумма вклада
        r = random.randint(100, 2000) / 10000  # ставка от 0.01 до 0.2
        p = random.randint(1, 10)  # срок в годах
        b = random.randint(20000, 25000)  # порог для бонуса

        deposit1 = DepositFactory.create_deposit(
            "Срочный вклад", amount=a, rate=r, period=p
        )
        deposit2 = DepositFactory.create_deposit(
            "Бонусный вклад", amount=a, rate=r, period=p,
            bonus_threshold=b, bonus_rate=0.09
        )
        deposit3 = DepositFactory.create_deposit(
            "Вклад со сложным процентом", amount=a, rate=r, period=p
        )
        l = 0
        global obj
        for dep in [deposit1, deposit2, deposit3]:
            temp = dep.calculate_profit()
            if temp > l:
                obj, l = dep, temp
            print(f"Денюшки были под вкладом {dep.__class__.__name__}: и мы получили прибыль = {temp:.2f} руб. за {dep.period} лет.")

        print(f"Самый выгодный вклад в данном случае - {obj.__class__.__name__} \n \n")


# C:\Users\korudenko\PycharmProjects\botconfectioner\.venv2\Scripts\python.exe C:\Users\korudenko\PycharmProjects\Py3semestr2025RudenkoKTmo2-16\laba4\Task4-1.py
# Денюшки были под вкладом FixedDeposit: и мы получили прибыль = 7692.19 руб. за 3 лет.
# Бонус!
# Денюшки были под вкладом BonusDeposit: и мы получили прибыль = 8384.49 руб. за 3 лет.
# Денюшки были под вкладом CompoundDeposit: и мы получили прибыль = 8106.28 руб. за 3 лет.
# Самый выгодный вклад в данном случае - BonusDeposit


# Денюшки были под вкладом FixedDeposit: и мы получили прибыль = 5626.17 руб. за 2 лет.
# Бонус!
# Денюшки были под вкладом BonusDeposit: и мы получили прибыль = 6132.53 руб. за 2 лет.
# Денюшки были под вкладом CompoundDeposit: и мы получили прибыль = 5799.46 руб. за 2 лет.
# Самый выгодный вклад в данном случае - BonusDeposit

# Денюшки были под вкладом FixedDeposit: и мы получили прибыль = 39176.57 руб. за 3 лет.
# Бонус!
# Денюшки были под вкладом BonusDeposit: и мы получили прибыль = 42702.46 руб. за 3 лет.
# Денюшки были под вкладом CompoundDeposit: и мы получили прибыль = 47003.31 руб. за 3 лет.
# Самый выгодный вклад в данном случае - CompoundDeposit

# Денюшки были под вкладом FixedDeposit: и мы получили прибыль = 11579.32 руб. за 3 лет.
# Бонус!
# Денюшки были под вкладом BonusDeposit: и мы получили прибыль = 12621.46 руб. за 3 лет.
# Денюшки были под вкладом CompoundDeposit: и мы получили прибыль = 12135.66 руб. за 3 лет.
# Самый выгодный вклад в данном случае - BonusDeposit

# Денюшки были под вкладом FixedDeposit: и мы получили прибыль = 1618.68 руб. за 4 лет.
# Денюшки были под вкладом BonusDeposit: и мы получили прибыль = 1618.68 руб. за 4 лет.
# Денюшки были под вкладом CompoundDeposit: и мы получили прибыль = 1756.40 руб. за 4 лет.
# Самый выгодный вклад в данном случае - CompoundDeposit


# Денюшки были под вкладом FixedDeposit: и мы получили прибыль = 76069.35 руб. за 6 лет.
# Бонус!
# Денюшки были под вкладом BonusDeposit: и мы получили прибыль = 82915.59 руб. за 6 лет.
# Денюшки были под вкладом CompoundDeposit: и мы получили прибыль = 108900.41 руб. за 6 лет.
# Самый выгодный вклад в данном случае - CompoundDeposit

# Денюшки были под вкладом FixedDeposit: и мы получили прибыль = 10027.08 руб. за 4 лет.
# Бонус!
# Денюшки были под вкладом BonusDeposit: и мы получили прибыль = 10929.52 руб. за 4 лет.
# Денюшки были под вкладом CompoundDeposit: и мы получили прибыль = 10724.44 руб. за 4 лет.
# Самый выгодный вклад в данном случае - BonusDeposit

# Денюшки были под вкладом FixedDeposit: и мы получили прибыль = 36998.19 руб. за 3 лет.
# Бонус!
# Денюшки были под вкладом BonusDeposit: и мы получили прибыль = 40328.03 руб. за 3 лет.
# Денюшки были под вкладом CompoundDeposit: и мы получили прибыль = 43319.66 руб. за 3 лет.
# Самый выгодный вклад в данном случае - CompoundDeposit

# Денюшки были под вкладом FixedDeposit: и мы получили прибыль = 17418.47 руб. за 5 лет.
# Бонус!
# Денюшки были под вкладом BonusDeposit: и мы получили прибыль = 18986.13 руб. за 5 лет.
# Денюшки были под вкладом CompoundDeposit: и мы получили прибыль = 18880.12 руб. за 5 лет.
# Самый выгодный вклад в данном случае - BonusDeposit

# Денюшки были под вкладом FixedDeposit: и мы получили прибыль = 65925.64 руб. за 10 лет.
# Бонус!
# Денюшки были под вкладом BonusDeposit: и мы получили прибыль = 71858.95 руб. за 10 лет.
# Денюшки были под вкладом CompoundDeposit: и мы получили прибыль = 113806.04 руб. за 10 лет.
# Самый выгодный вклад в данном случае - CompoundDeposit

# Process finished with exit code 0