#  Задание №3
def thesaurus(*args):
    names_list_in = list(args)
    names_list_in.sort()
    res_dict = {}
    for i in names_list_in:
        key_i = i[0]
        list_name = []
        if res_dict.get(key_i) is None:
            list_name.append(i)
            res_dict.setdefault(key_i, list_name)
        else:
            res_dict.get(key_i).append(i)
            res_dict.get(key_i).sort()
    return res_dict


print(thesaurus("Иван", "Мария", "Петр", "Илья", "Алена", "Аня", "Харитон"))
