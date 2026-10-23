
MAX_HEADS = 7


def max_power_dp(n, limit=MAX_HEADS):
    """Возвращает максимальное произведение слагаемых."""
    best = [0] * (n + 1)
    best[0] = 1

    for i in range(1, n + 1):
        for k in range(1, min(i, limit) + 1):
            best[i] = max(best[i], best[i - k] * k)

    return best[n]


def max_power_formula(n):
    """Возвращает максимальное произведение по формуле."""
    if n <= 4:
        return n

    if n % 3 == 0:
        return 3 ** (n // 3)

    if n % 3 == 1:
        return 4 * 3 ** ((n - 4) // 3)

    return 2 * 3 ** ((n - 2) // 3)


def max_power_brute(n):
    """Находит максимум полным перебором разбиений."""
    best = [0] * (n + 1)
    best[0] = 1

    for i in range(1, n + 1):
        for k in range(1, i + 1):
            best[i] = max(best[i], k * best[i - k])

    return best[n]


def test_max_power():
    for n in range(1, 100):
        assert max_power_dp(n) == max_power_formula(n), (
            f"Несовпадение с формулой при N = {n}"
        )

    for n in range(1, 26):
        assert max_power_dp(n) == max_power_brute(n), (
            f"Несовпадение с перебором при N = {n}"
        )

    print("Все 99 проверок по формуле пройдены.")
    print("Все 25 проверок полным перебором пройдены.")


def main():
    try:
        n = int(input("Введите N (0 < N < 100): "))
    except ValueError:
        print("Ошибка: необходимо ввести целое число.")
        return

    if not 0 < n < 100:
        print("Ошибка: N должно быть в диапазоне 0 < N < 100.")
        return

    print("Максимальная сила стаи:", max_power_dp(n))


if __name__ == "__main__":
    test_max_power()
    main()

