#  Задание №5
from random import choice

NOUNS = ["автомобиль", "лес", "огонь", "город", "дом"]
ADVERBS = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
ADJECTIVES = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]


def get_jokes(n):
    """Function return jokes
        Keyword arguments:
        n - count jokes gen.
        """
    jokes_list = []
    # jokes_list.append(" ".join([choice(NOUNS), choice(ADVERBS), choice(ADJECTIVES)]))
    for i in range(n):
        jokes_list.append(" ".join([choice(NOUNS), choice(ADVERBS), choice(ADJECTIVES)]))
    return jokes_list


print(get_jokes(2))

