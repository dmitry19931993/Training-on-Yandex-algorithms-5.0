seq_1 = int(input())
seq_2 = list(map(int, input().split()))
answer = ''
odd = 0
index = 0

for i in range(seq_1):
    answer += '+'
    if (seq_2[i] % 2) == 1:
        odd += 1
        index = i

if (odd % 2) == 0 and index == 0:
    answer = answer[:index] + 'x' + answer[index + 1:]

if (odd % 2) == 0 and index != 0:
    answer = answer[:index - 1] + 'x' + answer[index:]

answer = answer[:-1]

print(answer)