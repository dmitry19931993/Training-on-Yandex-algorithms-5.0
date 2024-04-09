seq_1 = int(input())

perimeter = 4 * seq_1
desk_list = []

x = (-1, 0, 1, 0)
y = (0, 1, 0, -1)

for _ in range(seq_1):
    seq_2 = list(map(int, input().split()))
    desk_list.append(seq_2)


for i in desk_list:
    for k in range(4):
        dif = [(i[0] + x[k]), i[1] + y[k]]
        if dif in desk_list:
            perimeter = perimeter - 1


print(perimeter)