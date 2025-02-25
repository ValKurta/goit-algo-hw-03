from datetime import datetime

def get_days_from_today(date):
    """
    Функція приймає один параметр: date — рядок, що представляє дату у форматі 'РРРР-ММ-ДД' (наприклад, '2020-10-09').
    Функція повертає ціле число, яке вказує на кількість днів від заданої дати до поточної. 
    Якщо задана дата пізніша за поточну, результат має бути від'ємним.
    У розрахунках необхідно враховувати лише дні, ігноруючи час (години, хвилини, секунди).
    Для роботи з датами слід використовувати модуль datetime Python.
    """
    tday = datetime.today()
    try:
        pday = datetime.strptime(date, '%Y-%m-%d')        
        result = (tday - pday).days

        return result
    except ValueError:
        print (f"{date} does not match format '%Y-%m-%d'")

print(get_days_from_today("2021-10-09"))
