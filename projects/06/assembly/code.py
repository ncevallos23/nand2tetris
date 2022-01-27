def dest(command):
    d = [0, 0, 0]
    if command == None:
        return d
    if 'M' in command:
        d[2] = 1
    if 'A' in command:
        d[0] = 1
    if 'D' in command:
        d[1] = 1

    return d

def comp(command):
    if command == '0':
        return [0, 1, 0, 1, 0, 1, 0]
    elif command == '1':
        return [0, 1, 1, 1, 1, 1, 1]
    elif command == '-1':
        return [0, 1, 1, 1, 0, 1, 0]
    elif command == 'D':
        return [0, 0, 0, 1, 1, 0, 0]
    elif command == 'A':
        return [0, 1, 1, 0, 0, 0, 0]
    elif command == '!D':
        return [0, 0, 0, 1, 1, 0, 1]
    elif command == '!A':
        return [0, 1, 1, 0, 0, 0, 1]
    elif command == '-D':
        return [0, 0, 0, 1, 1, 1, 1]
    elif command == '-A':
        return [0, 1, 1, 0, 0, 1, 1]
    elif command == 'D+1':
        return [0, 0, 1, 1, 1, 1, 1]
    elif command == 'A+1':
        return [0, 1, 1, 0, 1, 1, 1]
    elif command == 'D-1':
        return [0, 0, 0, 1, 1, 1, 0]
    elif command == 'A-1':
        return [0, 1, 1, 0, 0, 1, 0]
    elif command == 'D+A':
        return [0, 0, 0, 0, 0, 1, 0]
    elif command == 'D-A':
        return [0, 0, 1, 0, 0, 1, 1]
    elif command == 'A-D':
        return [0, 0, 0, 0, 1, 1, 1]
    elif command == 'D&A':
        return [0, 0, 0, 0, 0, 0, 0]
    elif command == 'D|A':
        return [0, 0, 1, 0, 1, 0, 1]
    elif command == 'M':
        return [1, 1, 1, 0, 0, 0, 0]
    elif command == '!M':
        return [1, 1, 1, 0, 0, 0, 1]
    elif command == '-M':
        return [1, 1, 1, 0, 0, 1, 1]
    elif command == 'M+1':
        return [1, 1, 1, 0, 1, 1, 1]
    elif command == 'M-1':
        return [1, 1, 1, 0, 0, 1, 0]
    elif command == 'D+M':
        return [1, 0, 0, 0, 0, 1, 0]
    elif command == 'D-M':
        return [1, 0, 1, 0, 0, 1, 1]
    elif command == 'M-D':
        return [1, 0, 0, 0, 1, 1, 1]
    elif command == 'D&M':
        return [1, 0, 0, 0, 0, 0, 0]
    elif command == 'D|M':
        return [1, 0, 1, 0, 1, 0, 1]
    else:
        return None


def jump(command):
    if command == None:
        return [0, 0, 0]
    elif command == 'JGT':
        return [0, 0, 1]
    elif command == 'JEQ':
        return [0, 1, 0]
    elif command == 'JGE':
        return [0, 1, 1]
    elif command == 'JLT':
        return [1, 0, 0]
    elif command == 'JNE':
        return [1, 0, 1]
    elif command == 'JLE':
        return [1, 1, 0]
    elif command == 'JMP':
        return [1, 1, 1]
    else:
        return None