import re

def normalize_phone(phone_number):
    # Видаляємо всі символи, крім цифр та '+'
    phone_number = re.sub(r'\D', '', phone_number)

    # Перевіряємо, чи номер починається з '+'
    if not phone_number.startswith('+'):
        # Якщо міжнародний код відсутній, додаємо код '+38'
        phone_number = '+38' + phone_number.lstrip('0')
    return phone_number