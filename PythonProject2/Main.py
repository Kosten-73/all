def solve():
    MOD = 10**9 + 7  # Не нужен для этой задачи, но оставим если вдруг понадобится для больших чисел

    # ===== Ввод данных прямо в код =====
    t = 2  # количество тестов
    test_cases = [
        (7, 21, [10, 20, 30, 40, 50, 60, 70]),
        (6, 500, [200, 200, 300, 500, 600, 600])
    ]
    # =================================

    for n, a, v in test_cases:
        v.sort()
        candidates = set()
        candidates.add(0)
        candidates.add(2 * 10**9)
        # добавляем середины между vi и a
        for vi in v:
            mid = (vi + a) // 2
            candidates.add(mid)
            candidates.add(mid + 1)

        best_b = 0
        max_score = -1

        for b in candidates:
            score = sum(abs(vi - b) < abs(vi - a) for vi in v)
            if score > max_score:
                max_score = score
                best_b = b

        print(f"Оптимальная ставка Банка 'Профит': {best_b}, очков: {max_score}")

solve()