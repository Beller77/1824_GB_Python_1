staff_data = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА',
              'токарь высшего разряда нИКОЛАй', 'директор аэлита']
for employee in staff_data:
    name_from_employee = employee.split()[-1].title()
    print(f'Привет, {name_from_employee}!')
