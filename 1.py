"""
1. Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
Напишите два варианта решения: через list и через dict.

Пример:
Введите номер месяца: 10
Результат через список: Осень
Результат через словарь: Осень
"""
number = int(input("Введите номер месяца: "))
add_list = ['зима', 'весна', 'лето', 'Осень']
add_dict = {1: 'зима', 2: 'зима', 3: 'весна', 4: 'весна', 5: 'весна', 6: 'лето',
            7: 'лето', 8: 'лето', 9: 'Осень', 10: 'Осень', 11: 'Осень', 12: 'зима'}

for i in range(1, 13):
    if i == number:
        print(f"Результат через список: {add_dict[i]}")

for i in range(1, 13):
    if i == number:
        match number:
            case 1:
                season = add_list[0]
            case 2:
                season = add_list[0]
            case 3:
                season = add_list[1]
            case 4:
                season = add_list[1]
            case 5:
                season = add_list[1]
            case 6:
                season = add_list[2]
            case 7:
                season = add_list[2]
            case 8:
                season = add_list[2]
            case 9:
                season = add_list[4]
            case 10:
                season = add_list[4]
            case 11:
                season = add_list[4]
            case 12:
                season = add_list[0]
print(f"Результат через словарь:{season}")
