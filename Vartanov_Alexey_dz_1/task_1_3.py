for i in range(1, 101):
    ending = ''
    n = i % 10
    if n == 0 or 4 < n <= 9:
        ending = 'ов'
    if n == 1:
        ending = ''
    if 1 < n < 5:
        ending = 'а'
    if 10 < i < 15:
        ending = 'ов'
    print(i, 'процент' + ending)
