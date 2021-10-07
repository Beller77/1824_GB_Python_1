duration = int(input('Введите кол-во секунд - '))
days = duration // 86400
hours = duration % 86400 // 3600
minutes = duration % 3600 // 60
seconds = duration % 60

time_list = [days, hours, minutes, seconds]
object_list = ['дн', 'час', 'мин', 'сек']
for i in range(len(time_list)):
    if time_list[i] != 0:
        print(time_list[i], object_list[i], end=' ')
