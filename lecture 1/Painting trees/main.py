seq_1 = list(map(int, input().split()))
seq_2 = list(map(int, input().split()))

tress_len = 0
seq_1_start = seq_1[0] - seq_1[1]
seq_1_stop = seq_1[0] + seq_1[1]
seq_2_start = seq_2[0] - seq_2[1]
seq_2_stop = seq_2[0] + seq_2[1]

if seq_1_start >= seq_2_start and seq_1_stop >= seq_2_stop and seq_2_stop >= seq_1_start:
    tress_len = seq_1_stop - seq_2_start + 1

elif seq_1_start <= seq_2_start and seq_1_stop >= seq_2_stop and seq_2_stop >= seq_1_start:
    tress_len = seq_1_stop - seq_1_start + 1


elif seq_1_start >= seq_2_start and seq_1_stop <= seq_2_stop and seq_1_stop >= seq_2_start:
    tress_len = seq_2_stop - seq_2_start + 1


elif seq_1_start <= seq_2_start and seq_1_stop <= seq_2_stop and seq_1_stop >= seq_2_start:
    tress_len = seq_2_stop - seq_1_start + 1

else:
    tress_len = (seq_1_stop - seq_1_start) + (seq_2_stop - seq_2_start) + 2

print(tress_len)