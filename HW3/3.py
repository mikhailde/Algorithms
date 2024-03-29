# Временная сложность: O(n)
# Алгоритм для вычисления средних значений на каждом уровне дерева


def average_of_levels(root):
    if root is None:
        return []  # Возвращаем пустой список, если дерево пустое

    averages = []  # Создаем список для хранения средних значений на каждом уровне
    current_level = [root]  # Инициализируем список текущего уровня с корневым узлом

    while current_level:
        level_sum = 0  # Переменная для хранения суммы значений узлов на текущем уровне
        level_count = len(current_level)  # Переменная для хранения количества узлов на текущем уровне
        next_level = []  # Создаем пустой список для хранения узлов следующего уровня

        for node in current_level:
            level_sum += node.val  # Суммируем значения узлов на текущем уровне

            if node.left:
                next_level.append(node.left)  # Добавляем левого потомка в список узлов следующего уровня

            if node.right:
                next_level.append(node.right)  # Добавляем правого потомка в список узлов следующего уровня

        level_average = level_sum / level_count  # Вычисляем среднее значение на текущем уровне
        averages.append(level_average)  # Добавляем среднее значение в список средних значений

        current_level = next_level  # Обновляем текущий уровень для следующей итерации

    return averages  # Возвращаем список средних значений на каждом уровне дерева

