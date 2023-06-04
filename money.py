for n in range(1,15):
    f = open(f'input{n}.txt')
    l = open(f'output{n}.txt')
    f1 = f.readlines()
    l1 = l.readlines()
    for i in range(len(f1)):
        f1[i] = f1[i].replace('\n', '')
        f1[i] = f1[i].split(' ')

    l1[0] = l1[0].split(' ')
    for i in range(len(l1[0])):
        l1[0][i] = int(l1[0][i])

    afirst = [int(elem) for elem in f1[0][1:]]
    bdfirst = list(reversed(sorted([int(elem) for elem in f1[1][1:]])))
    alast = list(reversed([int(elem) for elem in f1[2][1:]]))
    bdlast = (sorted([int(elem) for elem in f1[3][1:]]))
    money = [int(elem) for elem in f1[-1]]

    for i in range(len(money)):
        for j in range(len(bdfirst)):
            if money[i] >= bdfirst[j]:
                money[i] -= 1

    for i in range(len(money) - 1):
        money[i + 1] += money[i] * afirst[i]
    sum = money[-1]

    new_sum = []
    for j in range(len(alast)):
        new_sum.insert(0, sum % alast[j])
        sum = sum // alast[j]
    new_sum.insert(0, sum)

    for i in range(len(new_sum)):
        for j in range(len(bdlast)):
            if new_sum[i] >= bdlast[j]:
                new_sum[i] += 1

    if l1[0] == new_sum:
        print(f"true - {n}")
