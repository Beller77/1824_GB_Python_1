list1 = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
list2 = []
for i, val in enumerate(list1):
    sign_val = ''
    zero = ''
    if '+' in val or '-' in val:
        sign_val = val[0]
        val = val[1:]
    if val.isdigit():
        val = int(val)
        if val < 10:
            zero = '0'
        val = sign_val + zero + str(val)
        list2.append('"' + val + '"')
    else:
        list2.append(val)
print(list2)
row = ' '.join(list2)
print(row)
