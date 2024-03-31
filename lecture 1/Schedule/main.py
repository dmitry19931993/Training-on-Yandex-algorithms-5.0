seq_1 = int(input())
seq_2 = int(input())
day_off_list = []
year_list = []
year_dict = {}
week_dict = {}
days = 365
week_list = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

if ((seq_2 % 4) == 0 and (seq_2 % 100) != 0) or ((seq_2 % 100) == 0 and (seq_2 % 200) == 0):
    days = 366

for _ in range(seq_1):
    seq_3 = list(input().split())
    day_off_list.append(seq_3)

seq_4 = input()

for i in range(7):
    if week_list[i] == seq_4:
        start_day = i
    week_dict[week_list[i]] = 0

for _ in range(days):
    year_list.append(week_list[start_day])
    start_day = (start_day + 1) % 7

for i in year_list:
    week_dict[i] += 1

if days == 365:
    year_dict['January'] = year_list[:31]
    year_dict['February'] = year_list[31:59]
    year_dict['March'] = year_list[59:90]
    year_dict['April'] = year_list[90:120]
    year_dict['May'] = year_list[120:151]
    year_dict['June'] = year_list[151:181]
    year_dict['July'] = year_list[181:212]
    year_dict['August'] = year_list[212:243]
    year_dict['September'] = year_list[243:273]
    year_dict['October'] = year_list[273:304]
    year_dict['November'] = year_list[304:334]
    year_dict['December'] = year_list[334:]

if days == 366:
    year_dict['January'] = year_list[:31]
    year_dict['February'] = year_list[31:60]
    year_dict['March'] = year_list[60:91]
    year_dict['April'] = year_list[91:121]
    year_dict['May'] = year_list[121:152]
    year_dict['June'] = year_list[152:182]
    year_dict['July'] = year_list[182:213]
    year_dict['August'] = year_list[213:244]
    year_dict['September'] = year_list[244:274]
    year_dict['October'] = year_list[274:305]
    year_dict['November'] = year_list[305:335]
    year_dict['December'] = year_list[335:]


for i in day_off_list:
    day = year_dict[i[1]][int(i[0]) - 1]
    week_dict[day] = week_dict[day] - 1

sorted_week = sorted(week_dict.items(), key=lambda item: item[1])
answer = sorted_week[6][0] + ' ' + sorted_week[0][0]


print(answer)