import sys
sys.set_int_max_str_digits(0)

seq = list(map(int, input().split()))
total = seq[0]
count = 0

for i in range(seq[2]):
    total_4 = total * 10
    total_1 = total_4 % seq[1]
    total_2 = seq[1] - total_1
    if total_1 == 0:
        total = total_4
        count += 1
        if count == 2:
            total = total * (10 ** (seq[2] - i - 1))
            break
    elif total_2 < 10:
        total = total_4 + total_2
    else:
        total = -1
        break

print(total)