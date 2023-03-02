array = list(map(int, input('Введите любую последовательность чисел через пробел от 0 до 999:').split()))
number = int(input("Введите число от 1 до 999: "))

while number:
    if number <= min(array):
        print('Введённое Вами число меньше мин.числа, введённого Вами в последовательности.\n '
              'Введите число, которое будет не меньше минимального: ')

        number = int(input('Введите число, соответствующее критериям поиска:'))
    elif number > max(array):
        print('Введённое Вами число больше макс.значения, введённого Вами в последовательности \n '
              'Введите число, которое будет не больше максимального : ')

        number = int(input('Введите число, соответствующее критериям поиска:'))
    else:
        break

def merge_sort(array):                    # "разделяй"
    if len(array) < 2:                    # если кусок массива равен 2,
        return array[:]                    # выход из рекурсии
    else:
        middle = len(array) // 2            # ищем середину
        left = merge_sort(array[:middle])              # рекурсивно делим левую часть
        right = merge_sort(array[middle:])  # и правую
        return merge(left, right)           # выполняем слияние

def merge(left, right):
    result = []
    i, j = 0, 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    while i < len(left):
        result.append(left[i])
        i += 1

    while j < len(right):
        result.append(right[j])
        j += 1

    return result

print(merge_sort(array))

def bi_search(array, number, left, right):
    if left > right or number == max(array) or number == min(array):
        return False

    middle = (right + left) // 2      # находимо середину
    if array[middle] == number:            # если элемент в середине,
        return middle
    elif number < array[middle]:               # если элемент меньше элемента в середине
        # рекурсивно ищем в левой половине
        return bi_search(array, number, left, middle -1)
    else: # иначе в правой
        return bi_search(array, number, right, middle +1)

print(bi_search(array, number, 0, len(array)))