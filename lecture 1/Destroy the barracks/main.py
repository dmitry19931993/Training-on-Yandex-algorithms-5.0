seq_1 = int(input())
seq_2 = int(input())
seq_3 = int(input())
my_solger = seq_1
helth_barac = seq_2 - seq_1
enemy_solger = seq_3
count = 1
count_list = []
count_list_answer = []

if helth_barac > 0:
    while True:
        count += 1
        if helth_barac > my_solger and enemy_solger >= my_solger:
            count = -1
            count_list.append(count)
            break
        elif helth_barac > my_solger and enemy_solger < my_solger:
            helth_barac = helth_barac - (my_solger - enemy_solger)

        elif helth_barac == 0 or (helth_barac / my_solger) < 0.05:
            enemy_solger = enemy_solger - (my_solger - helth_barac)
            helth_barac = 0
            my_solger = my_solger - enemy_solger
        elif helth_barac <= my_solger and enemy_solger == my_solger:
            enemy_solger = enemy_solger - (my_solger - helth_barac)
            helth_barac = 0
            my_solger = my_solger - enemy_solger
            if enemy_solger <= 0:
                count_list.append(count)
                break
            if my_solger <= 0:
                count = -1
                count_list.append(count)
                break
        elif helth_barac <= my_solger and helth_barac > 0:
            enemy_solger = enemy_solger - (my_solger - helth_barac)
            if (enemy_solger / my_solger) > 0.6666 and helth_barac > 0:
                enemy_solger = enemy_solger + (my_solger - helth_barac)
                if enemy_solger < my_solger:
                    helth_barac = helth_barac - (my_solger - enemy_solger)
                else:
                    count = -1
                    count_list.append(count)
                    break
            else:
                enemy_solger = enemy_solger + (my_solger - helth_barac)
                my_solger_next = my_solger
                enemy_solger_next = enemy_solger
                helth_barac_next = helth_barac
                count_next = count
                while enemy_solger_next > 0:
                    enemy_solger_next = enemy_solger_next - (my_solger_next - helth_barac_next)
                    helth_barac_next = 0
                    my_solger_next = my_solger_next - enemy_solger_next
                    count_next += 1
                    if my_solger_next <= 0:
                        enemy_solger_next = 0
                        count_next = -1
                    if enemy_solger_next <= 0:
                        helth_barac = helth_barac - (my_solger - enemy_solger)
                        count_list.append(count_next - 1)
        if helth_barac <= 0 and enemy_solger <= 0:
            count_list.append(count)
            break
else:
    count_list.append(count)

for i in count_list:
    if i >= 0:
        count_list_answer.append(i)

if count_list_answer:
    answer = count_list_answer[0]
    for i in count_list_answer:
        if answer > i:
            answer = i
else:
    answer = -1

print(answer)