seq_1 = int(input())


berry_sum = 0
berry_str = ''
berry_list = []
berry_list_negative = []
berry_str_negative = ''
berry_list_unic = [0, [0, 0], 0]
berry_negative_list_unic = [0, [0, 0]]
hight_max = 0


for i in range(1, seq_1 + 1):
    seq_2 = list(map(int, input().split()))
    if seq_2[0] >= seq_2[1]:
        difference = seq_2[0] - seq_2[1]
        if seq_2[0] - berry_list_unic[1][0] >= difference - berry_list_unic[2]:
            berry_sum = berry_sum + berry_list_unic[2]
            berry_list.append(berry_list_unic[0])
            berry_list_unic = [i, seq_2, difference]
        else:
            berry_sum = berry_sum + difference
            berry_list.append(i)
    elif seq_2[0] < seq_2[1]:
        if seq_2[0] > berry_negative_list_unic[1][0]:
            berry_list_negative.append(berry_negative_list_unic[0])
            berry_negative_list_unic = [i, seq_2]
        else:
            berry_list_negative.append(i)

berry_sum = berry_sum + berry_list_unic[1][0]
if hight_max < berry_sum:
    hight_max = berry_sum
berry_sum = berry_sum - berry_list_unic[1][1]
berry_list.append(berry_list_unic[0])

if berry_list_negative:
    berry_sum = berry_sum + berry_negative_list_unic[1][0]
    if hight_max < berry_sum:
        hight_max = berry_sum
    berry_list.append(berry_negative_list_unic[0])
    berry_list = berry_list + berry_list_negative[1:]


print(hight_max)
print(' '.join(map(str, berry_list[1:])))