seq_1 = int(input())


x_max = -(10 ** 10)
x_min = 10 ** 10

y_max = -(10 ** 10)
y_min = 10 ** 10

for i in range(seq_1):
    seq_2 = list(map(int, input().split()))
    if seq_2[0] > x_max:
        x_max = seq_2[0]
    if seq_2[1] > y_max:
        y_max = seq_2[1]
    if seq_2[0] < x_min:
        x_min = seq_2[0]
    if seq_2[1] < y_min:
        y_min = seq_2[1]

print(str(x_min) + " " + str(y_min) + " " + str(x_max) + " " + str(y_max) )