message_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
print(f"id списка до преобразований: {id(message_list)}")
pos_in_list = 0
while pos_in_list <= (len(message_list) - 1):
    val = message_list[pos_in_list]
    sign = ''
    if "+" in val or "-" in val:
        sign = val[0]
        val = val.replace(sign, '')
    if val.isdigit():
        message_list[pos_in_list] = f'{sign}{int(val):02d}'
        message_list.insert(pos_in_list, '"')
        message_list.insert(pos_in_list + 2, '"')
        pos_in_list += 1
    else:
        pass
    pos_in_list += 1
print(message_list)
status_quote = False
for show_val in message_list:
    if (show_val != '"' and not status_quote) or (show_val == '"' and status_quote):
        status_quote = False
        print(show_val, end=' ')
    elif show_val == '"' and not status_quote:
        status_quote = True
        print(show_val, end='')
    else:
        print(show_val, end='')
print(f"\nid списка после преобразований: {id(message_list)}")
