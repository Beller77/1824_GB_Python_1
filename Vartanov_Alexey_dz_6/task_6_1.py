list_tuple = []
with open('nginx_logs.txt', 'r', encoding='utf-8') as f:
    for line in f:
        line = line.split()
        list_tuple.append((line[0], line[5].replace('"', ''), line[6].replace('"', '')))
print(list_tuple)
