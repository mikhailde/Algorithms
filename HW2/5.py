# Сложность алгоритма: O(n), где n - количество элементов в массиве цен.
# Создается список num длиной, равной длине списка prices, и заполняется значениями 1. Каждый элемент списка num представляет количество гладких спусковых периодов, начинающихся с соответствующего элемента списка prices.
# Затем происходит итерация по индексам списка num начиная с индекса 1. Для каждого индекса проверяется, является ли разница между предыдущим и текущим элементами списка prices равной 1. Если это условие выполняется, то обновляется значение текущего элемента списка num, добавляя 1 к значению предыдущего элемента, так как это означает, что найден гладкий спусковой период.
# В конце функция возвращает сумму всех элементов списка num, что представляет общее количество гладких спусковых периодов.

def getDescentPeriods(prices) -> int:
    num = [1] * len(prices)                 # Создаем список из 1 длиной списка prices
    for i in range(1, len(num)):             # Итерируемся по индексам списка num, начиная с индекса 1
        if prices[i - 1] - prices[i] == 1:   # Проверяем, является ли разница между предыдущим и текущим элементами списка prices равной 1
            num[i] = num[i - 1] + 1          # Если да, то обновляем значение текущего элемента списка num, добавляя 1 к значению предыдущего элемента

    return sum(num)                          # Возвращаем сумму всех элементов списка num