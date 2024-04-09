seq_1 = int(input())

seq_2 = list(map(int, input().split()))

line_max = seq_2[0]
line_sum = 0

for i in seq_2:
    if i > line_max:
        line_max = i

    line_sum += i
var_1 = line_max - (line_sum - line_max)
var_2 = line_sum

if var_1 >= 1 and var_1 < var_2:
    answer = var_1

else:
    answer = var_2

print(answer)
