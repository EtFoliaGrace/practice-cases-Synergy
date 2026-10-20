def sum_negative_between_max_min(a):
    """Сумма отрицательных между максимумом и минимумом."""
    if len(a) < 3:
        return 0
    i_max = a.index(max(a))   # первое вхождение максимума
    i_min = a.index(min(a))   # первое вхождение минимума
    left, right = sorted((i_max, i_min))
    return sum(x for x in a[left + 1:right] if x < 0)


def main():
    n = int(input("Введите N: "))
    a = list(map(float, input("Введите элементы: ").split()))
    if len(a) != n:
        print("Ошибка: количество элементов не равно N")
        return
    print("Сумма:", sum_negative_between_max_min(a))


if __name__ == "__main__":
    main()
