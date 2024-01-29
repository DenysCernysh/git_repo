import random

def get_numbers_ticket(min_num, max_num, quantity):
    # Перевірка вхідних параметрів
    if min_num < 1 or max_num > 1000 or quantity < min_num or quantity > max_num:
        return []  # Повертаємо пустий список, якщо параметри не відповідають обмеженням

    numbers = set()  # Створюємо множину для збереження унікальних чисел
    while len(numbers) < quantity:  # Поки не набрано достатню кількість чисел
        numbers.add(random.randint(min_num, max_num))  # Додаємо випадкове число до множини

    return sorted(list(numbers))  # Повертаємо відсортований список унікальних чисел