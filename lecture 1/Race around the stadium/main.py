l, x_1, v_1, x_2, v_2 = map(int, input().split())

ans = 10 ** 30

for rotation in range(2):
    deltax = (x_2 - x_1 + l) % l
    deltav = v_1 - v_2
    if deltav < 0:
        deltav = -deltav
        deltax = (-deltax) % l

    if deltax == 0:
        ans = 0

    if deltav != 0:
        ans = min(ans, deltax / deltav)

    x_2 = (-x_2) % l
    v_2 = -v_2

if ans == 10 ** 30:
    print('NO')

else:
    print('YES')
    print(ans)