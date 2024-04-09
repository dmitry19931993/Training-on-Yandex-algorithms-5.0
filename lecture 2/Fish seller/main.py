seq_1 = list(map(int, input().split()))
seq_2 = list(map(int, input().split()))

price_max = 0
profit_max = 0
difference = seq_1[1]


if seq_1[0] <= seq_1[1]:
    difference = seq_1[0] - 1



for i in range(seq_1[0]):
    for p in range((i + 1), (i + difference + 1)):
        if seq_2[p] >= price_max:
            price_max = seq_2[p]
    if seq_2[i] < price_max:
        if (price_max - seq_2[i]) > profit_max:
            profit_max = (price_max - seq_2[i])

    price_max = 0

    if (i + difference + 1) > (seq_1[0] - 1):
        difference = difference - 1



print(profit_max)
