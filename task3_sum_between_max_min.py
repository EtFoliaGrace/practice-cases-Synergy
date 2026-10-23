
def sum_negative_between_max_min(a):
    """Сумма отрицательных между максимумом и минимумом."""
    if len(a) < 3:
        return 0

    i_max = a.index(max(a))
    i_min = a.index(min(a))

    left, right = sorted((i_max, i_min))

    return sum(x for x in a[left + 1:right] if x < 0)


def test_sum_negative_between_max_min():
    tests = [
        ([3, -1, -2, 9, -5, -6, 1, -7], -11),
        ([-5, 2, -1, -3, 8], -4),
        ([4, -1, -2, -3, -10], -6),
        ([-1, -2, -3, 10, -4, -5, -20], -9),
        ([1, 2, 3], 0),
        ([7, 7, 7], 0),
        ([1, 5, 3], 0),
        ([5, -2, 5, -3, 1], -2),
        ([1, -4, -3, 5, 5], -7),
        ([5, 1, -2, -3, 1], -5),
        ([1, 2], 0),
        ([], 0),
    ]

    for array, expected in tests:
        result = sum_negative_between_max_min(array)
        assert result == expected, (
            f"Массив {array}: ожидалось {expected}, получено {result}"
        )

    print("Все автоматические тесты пройдены.")


def main():
    try:
        n = int(input("Введите N: "))
    except ValueError:
        print("Ошибка: N должно быть целым числом.")
        return

    if n <= 0:
        print("Ошибка: N должно быть больше нуля.")
        return

    try:
        a = list(map(int, input("Введите элементы: ").split()))
    except ValueError:
        print("Ошибка: элементы должны быть целыми числами.")
        return

    if len(a) != n:
        print("Ошибка: количество элементов не равно N.")
        return

    print("Сумма:", sum_negative_between_max_min(a))


if __name__ == "__main__":
    test_sum_negative_between_max_min()
    main()
