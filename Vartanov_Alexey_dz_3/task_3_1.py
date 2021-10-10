#  Задание №1
DICT_ENG_RU = {
    'one': 'один',
    'two': 'два',
    'three': 'три',
    'four': 'четыре',
    'five': 'пять',
    'six': 'шесть',
    'seven': 'семь',
    'eight': 'восемь',
    'nine': 'девять',
    'ten': 'десять'
}


def num_translate(num_eng):
    """ Если слово не будет найдено, то вернет None.
     Регистр букв не учитывается"""

    return DICT_ENG_RU.get(num_eng)


user_word = input("Введите числительное от 1 до 10 на английском языке: ")
print(num_translate(user_word))
