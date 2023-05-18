with open('input_s1_09.txt') as f:
    line = f.readline().split()
print(line)
    

def TayKitWord(word):
    new_word = ""
    help_word = list(word)
    if len(word)%2 == 0:
        for i in range(len(word)):
            n = len(help_word)// 2
            new_word += help_word[n]
            help_word.pop(n)
    else:
        for i in range(len(word)):
            if len(help_word) % 2 == 0:
                n = len(help_word)// 2 - 1
                new_word += help_word[n]
                help_word.pop(n)
            else:
                n = len(help_word)// 2
                new_word += help_word[n]
                help_word.pop(n)
    return(new_word)


def TayKitLine(line):
    new_line = ""
    help_line = line
    if len(help_line)%2 == 0:
        for i in range(len(line)):
            n = len(help_line)// 2
            new_line += TayKitWord(help_line[n])
            help_line.pop(n)
            new_line += ' '
    else:
        for i in range(len(line)):
            if len(help_line) % 2 == 0:
                n = len(help_line)// 2 - 1
                new_line += TayKitWord(help_line[n])
                help_line.pop(n)
                new_line += ' '
            else:
                n = len(help_line)// 2
                new_line += TayKitWord(help_line[n])
                help_line.pop(n)
                new_line += ' '
    print(new_line)

TayKitLine(line)


            
            
        
    