MAX_HEADS = 7  # максимум голов у одного дракона


def max_power_dp(n, limit=MAX_HEADS):
    """best[i] - максимальная сила стаи при сумме голов i."""
    best = [0] * (n + 1)
    best[0] = 1
    for i in range(1, n + 1):
        for k in range(1, min(i, limit) + 1):  # k голов у дракона
            best[i] = max(best[i], best[i - k] * k)
    return best[n]


def max_power_formula(n):
    """Проверка: разбиение на тройки по формуле."""
    if n <= 4:
        return n
    if n % 3 == 0:
        return 3 ** (n // 3)
    if n % 3 == 1:
        return 4 * 3 ** ((n - 4) // 3)
    return 2 * 3 ** ((n - 2) // 3)



def main():
    n = int(input("Введите N (0 < N < 100): "))

    if not 0 < n < 100:
        print("Ошибка: N должно быть в диапазоне 0 < N < 100")
        return

    dp_result = max_power_dp(n)
    formula_result = max_power_formula(n)

    if dp_result != formula_result:
        print("Ошибка: результаты не совпадают")
        return

    print(dp_result)


if __name__ == "__main__":
    main()
