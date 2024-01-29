from datetime import datetime, timedelta

def get_upcoming_birthdays(users):
    today = datetime.today().date()
    upcoming_birthday_users = []

    for user in users:
        # Конвертуємо рядок з датою народження в об'єкт datetime
        birthday_date = datetime.strptime(user["birthday"], "%Y.%m.%d").date()

        # Перевіряємо, чи вже минув день народження в цьому році
        if birthday_date < today.replace(year=birthday_date.year):
            # Якщо так, розглядаємо дату на наступний рік
            birthday_date = birthday_date.replace(year=today.year + 1)

        # Визначаємо різницю між днем народження та поточним днем
        days_until_birthday = (birthday_date - today).days

        # Перевіряємо, чи день народження випадає протягом наступного тижня
        if 0 <= days_until_birthday <= 7:
            # Якщо день народження припадає на вихідний, переносимо дату привітання на понеділок
            if birthday_date.weekday() >= 5:
                days_until_birthday += (7 - birthday_date.weekday())
                birthday_date += timedelta(days=days_until_birthday)

            # Додаємо ім'я користувача та відповідну дату привітання до списку
            upcoming_birthday_users.append(
                {"name": user["name"], "congratulation_date": birthday_date.strftime("%Y.%m.%d")})

    return upcoming_birthday_users