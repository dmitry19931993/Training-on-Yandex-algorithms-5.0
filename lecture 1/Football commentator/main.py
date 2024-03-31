seq_1 = list(map(int, input().split(':')))
seq_2 = list(map(int, input().split(':')))
seq_3 = int(input())

team_1 = seq_1[0] + seq_2[0]
team_2 = seq_1[1] + seq_2[1]

if team_1 < team_2 and seq_3 == 2:
    if seq_1[0] <= seq_2[1]:
        total = team_2 - team_1 + 1
    else:
        total = team_2 - team_1

elif team_1 < team_2 and seq_3 == 1:
    if seq_1[1] > seq_2[0] and (seq_1[1] - (team_2 - team_1)) >= seq_2[0]:
        total = team_2 - team_1 + 1
    else:
        total = team_2 - team_1

elif team_1 == team_2 and seq_3 == 2:
    if seq_1[0] <= seq_2[1]:
        total = 1
    else:
        total = 0

elif team_1 == team_2 and seq_3 == 1:
    if seq_1[1] >= seq_2[0]:
        total = 1
    else:
        total = 0

elif team_1 > team_2:
    total = 0

print(total)