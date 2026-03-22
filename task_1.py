my_string = '1h 45m,360s,25m,30m 120s,2h 60s'  # base string
my_list = my_string.split(',')  # split string in list time
result = 0  # result
for timing in my_list:
    list_time = timing.split(' ')
    for i in list_time:
        if 'h' in i:
            # calc minute in hours and add
            result += int(i.replace('h', ''))*60
        elif 'm' in i:
            result += int(i.replace('m', ''))  # add minute
        else:
            result += int(i.replace('s', ''))/60  # calc minute in sec and add
print(f'Общее количество минут = {result}')
