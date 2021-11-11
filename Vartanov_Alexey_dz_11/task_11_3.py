list_val = []


class OwnError(Exception):
    def __init__(self, numm):
        self.num = numm
        try:
            list_val.append(float(numm))
        except:
            print("Вы ввели не число!")


while True:
    num = input('Введите число для добавления в список: ')
    try:
        raise OwnError(num)
    except OwnError as err:
        if str(err) == 'stop':
            break

print(list_val)
