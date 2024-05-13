
# Задача 1

input_string = input("Кодирование строки. Введите строку символов: ")
encoded_string = ""
count = 1
for i in range(1, len(input_string)+1):
    if i == len(input_string) or input_string[i] != input_string[i - 1]:
        if count > 1:
            encoded_string += input_string[i - 1] + str(count)
            count = 1
        else:
            encoded_string += input_string[i - 1]
    else:
        count += 1
print(encoded_string)

# Задача 1.1
from string import ascii_letters

encoded_string = input("Декодирование строки.Введите закодированную строку: ")
decoded_string = ""
i = 0
while i < len(encoded_string):
    char = encoded_string[i]
    if char in ascii_letters:
        decoded_string += char
        i += 1
        if i < len(encoded_string) and encoded_string[i].isdigit():
            count = int(encoded_string[i])-1
            decoded_string += char * count
            i += 1
    else:
        i += 1

print(decoded_string)


#Задача 2: Поиск 3 наиболее часто встречающихся символов


from collections import Counter

input_string = input("Поиск 3 наиболее часто встречающихся символов. Введите строку: ")
string = input_string.replace(" ", "")
counter = Counter(string)
top_3 = counter.most_common(3)
print("Наиболее часто встречающиеся символы:")
for char, count in top_3:
    print(f"{char}: {count}")
#3
units = ['', 'один', 'два', 'три', 'четыре', 'пять', 'шесть', 'семь', 'восемь', 'девять']
teens = ['десять', 'одиннадцать', 'двенадцать', 'тринадцать', 'четырнадцать', 'пятнадцать', 'шестнадцать', 'семнадцать',
'восемнадцать', 'девятнадцать']
tens = ['', '', 'двадцать', 'тридцать', 'сорок', 'пятьдесят', 'шестьдесят', 'семьдесят', 'восемьдесят', 'девяносто']
hundreds = ['', 'сто', 'двести', 'триста', 'четыреста', 'пятьсот', 'шестьсот', 'семьсот', 'восемьсот', 'девятьсот']

number = int(input("Письменная запись числа. Введите число от 1 до 1000: "))

if number == 0:
    number_words = 'ноль'
elif number < 0 or number > 1000:
    (number_words) = 'Число должно быть в диапазоне от 1 до 1000.'
elif number < 10:
    number_words = units[number]
elif number < 20:
    number_words = teens[number - 10]
elif number < 100:
    number_words = tens[number // 10] + ' ' + units[number % 10]
elif number < 1000:
    number_words = hundreds[number // 100] + ' ' + tens[(number % 100)//10] + ' ' + units[number % 10]
elif number == 1000:
    number_words = 'тысяча'

print(number_words)




