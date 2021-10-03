user_lst = [x ** 3 for x in range(1, 1001) if x % 2 == 1]
user_sum = 0
for i in range(len(user_lst)):
    n = int(user_lst[i])
    user_sum_int = 0
    while n > 0:
        m = n % 10
        user_sum_int = user_sum_int + m
        n = n // 10
    if user_sum_int % 7 == 0:
        user_sum = user_sum + user_lst[i]
print(user_sum)
# Следующая часть задания:
user_lst2 = [x ** 3 + 17 for x in range(1, 1001) if x % 2 == 1]
user_sum = 0
for i in range(len(user_lst2)):
    n = int(user_lst2[i])
    user_sum_int = 0
    while n > 0:
        m = n % 10
        user_sum_int = user_sum_int + m
        n = n // 10
    if user_sum_int % 7 == 0:
        user_sum = user_sum + user_lst2[i]
print(user_sum)
# Следующая часть задания:
# '* Решить задачу под пунктом b, не создавая новый список.
user_lst = [x ** 3 for x in range(1, 1001) if x % 2 == 1]
user_sum1, user_sum2 = 0, 0
for i in range(len(user_lst)):
    n1 = int(user_lst[i])
    user_sum_int1 = 0
    n2 = int(user_lst[i] + 17)
    user_sum_int2 = 0
    while n1 > 0:
        m1 = n1 % 10
        user_sum_int1 = user_sum_int1 + m1
        n1 = n1 // 10
    if user_sum_int1 % 7 == 0:
        user_sum1 = user_sum1 + user_lst[i]
    while n2 > 0:
        m2 = n2 % 10
        user_sum_int2 = user_sum_int2 + m2
        n2 = n2 // 10
    if user_sum_int2 % 7 == 0:
        user_sum2 = user_sum2 + user_lst[i] + 17
print(user_sum1, user_sum2, sep='\n')
