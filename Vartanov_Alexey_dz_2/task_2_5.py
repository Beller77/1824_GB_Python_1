price_list = [57.8, 46.51, 97, 200.93, 5.64, 500, 20.8, 17.5,
              12.6, 50.5, 35.12, 12.5, 14.30, 30.10, 20, 20.21,
              1000.54, 100.25, 3.15, 15.20]

print(f'Задание А\n')
for num, price in enumerate(price_list):
    rub = int(price)
    cent = round(price % 1 * 100)
    print(f'{num + 1}) {rub:2d} руб. {cent:02d} коп.', end=' ')
print('\n')

print(f'Задание B\n')

id_in = id(price_list)
price_list.sort()
id_out = id(price_list)
print(f'id списка до сортировки: {id_in}\n'
      f'id спика после сортировки: {id_out}\n'
      f'Результат сравнения: {id_in == id_out}'
      )
for num, price in enumerate(price_list):
    rub = int(price)
    cent = round(price % 1 * 100)
    print(f'{num + 1}) {rub:2d} руб. {cent:02d} коп.', end=' ')
print('\n')


print(f'Задание С\n')
price_list_new = sorted(price_list, reverse=True)
print('Создан новый список, но отсортированный по убыванию - id списка:', id(price_list_new))
print(price_list_new)
for num, price in enumerate(price_list_new):
    rub = int(price)
    cent = round(price % 1 * 100)
    print(f'{num + 1}) {rub:2d} руб. {cent:02d} коп.', end=' ')
print('\n')


print(f'Задание D\n')
for num, price in enumerate(price_list_new[:5:1]):
    print(f'{num + 1}) {int(price):2d} руб. {round(price % 1 * 100):02d} коп.',
          end=', ')
print('\n')
