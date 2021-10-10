#  Задание №2
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


def num_translate_adv(num_eng):
    if num_eng.istitle():
        return DICT_ENG_RU.get(num_eng.lower()).title()
    else:
        return DICT_ENG_RU.get(num_eng)


user_word = input("Введите числительное от 1 до 10 на английском языке: ")
print(num_translate_adv(user_word))

