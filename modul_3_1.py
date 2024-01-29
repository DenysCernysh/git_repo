# 1. імпорт модуля datetime
from datetime import datetime

# 2. Перетворення рядка дати у форматі 'РРРР-ММ-ДД' у об'єкт datetime
date_string = '2020-10-09'
date_object = datetime.strptime(date_string, '%Y-%m-%d')

# 3.Отримання поточної дати
current_date = datetime.today()

# 4. Розрахунок різниці між поточною датою та заданою датою
date_difference = date_object - current_date

# 5. Повернення різниці у днях як ціле число. Використовуємо abs, щоб отримати додатне число
print(abs(date_difference.days))
