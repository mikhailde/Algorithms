# Временная сложность: O(n), где n - количество элементов в списке costs.

# Объяснение алгоритма:
# 1. Алгоритм сортирует список costs по разнице между стоимостью перелета в первый и второй города (c[0] - c[1]).
#    Это позволяет определить, для какого города стоимость перелета меньше.
# 2. Далее алгоритм разделяет отсортированный список на две части: первые L элементов, соответствующие более дешевым городам,
#    и оставшиеся L элементов, соответствующие более дорогим городам.
# 3. Наконец, алгоритм возвращает сумму стоимостей перелетов в первые L элементов списка (для более дешевых городов) и сумму
#    стоимостей перелетов в оставшихся L элементов списка (для более дорогих городов), что представляет собой минимальную
#    стоимость полетов для размещения людей в двух городах так, чтобы общая стоимость была минимальной.

def twoCitySchedCost(costs) -> int:
    # Сортируем список costs по разнице между стоимостью перелета в первый и второй города
    costs = sorted(costs, key=lambda a: a[0] - a[1])
    
    # Вычисляем количество элементов в списке
    L = len(costs) // 2
    
    # Суммируем стоимость перелетов для первых L элементов (более дешевые города)
    cost_first_city = sum(c[0] for c in costs[:L])
    
    # Суммируем стоимость перелетов для оставшихся L элементов (более дорогие города)
    cost_second_city = sum(c[1] for c in costs[L:])
    
    # Возвращаем общую минимальную стоимость полетов
    return cost_first_city + cost_second_city

