for i in range(0,10):
    a = 'input' + str(i+1) + '.txt'
    f = open(a)
    th = []
    while True:
        p = f.readline()
        if not p:
            break
        line = []
        line = p.split(' ')
        b = ''
        if line[0] == 'MIX':
            b = 'MX'
            for i in range(1,len(line)):
                if line[i].isdigit():
                    b = b + th[int(line[i])-1]
                else:
                    b = b + line[i].replace('\n', '')
            b = b + 'XM'
            th.append(b)
        elif line[0] == 'WATER':
            b = 'WT'
            for i in range(1,len(line)):
                if line[i].isdigit():
                    b = b + th[int(line[i])-1]
                else:
                    b = b + line[i].replace('\n', '')
            b = b + 'TW'
            th.append(b)
        elif line[0] == 'DUST':
            b = 'DT'
            for i in range(1,len(line)):
                if line[i].isdigit():
                    b = b + th[int(line[i])-1]
                else:
                    b = b + line[i].replace('\n', '')
            b = b + 'TD'
            th.append(b)
        elif line[0] == 'FIRE':
            b = 'FR'
            for i in range(1,len(line)):
                if line[i].isdigit():
                    b += th[int(line[i])-1]
                else:
                    b += line[i].replace('\n', '')
            b = b + 'RF'
            th.append(b)
    print(th[-1])
