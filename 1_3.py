def normalize_phone(phone_number):
    """
    Параметр функції phone_number - це рядок з телефонним номером у різноманітних форматах.
    Функція видаляє всі символи, крім цифр та символу '+'.
    Якщо міжнародний код відсутній, функція додає код '+38'.
    Функція повертає нормалізований телефонний номер у вигляді рядка.
    """    
    allowed_chars = '+0123456789'
    res = ''.join(char for char in phone_number if char in allowed_chars)
    if res.startswith('0'):
        res = '+38' + res
    elif res.startswith('80'):
        res =  '+3' + res    
    elif res.startswith('380'):
        res =  '+' + res
        
    if len(res) == 13:
        return res
    else:
        return f'{res} is wrong phone number'
    

raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567123123123",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)
