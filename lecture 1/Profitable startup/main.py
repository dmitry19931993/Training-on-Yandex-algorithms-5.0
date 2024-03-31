seq_1 = int(input())
total= 0
for _ in range(seq_1):
    seq_2 = int(input())
    while seq_2 >= 4:
        total += seq_2 // 4
        seq_2 = seq_2 % 4
    while seq_2 >= 3:
        total += 2 * (seq_2 // 3)
        seq_2 = seq_2 % 3
    total += seq_2

print(total)