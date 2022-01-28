def initalize():
    file = input("file>")
    f = open(file, 'r')
    lines = []
    for line in f:
        if line == '\n':
            continue
        if line[0:2] != '//':
            lines.append(line.strip().split()[0])

    return lines

def hasMoreCommands(index, file):
    if index != len(file) - 1:
        return False
    return True

def advance(file, index):
    if hasMoreCommands(index, file):
        index += 1
        return file[index], index

def commandType(command):
    if command[0] == '@':
        return 'A_COMMAND'
    elif command[0] == '(':
        return 'L_COMMAND'
    else:
        return 'C_COMMAND'

def symbol(command):
    if commandType(command) == 'A_COMMAND':
        return command[1:]
    elif commandType(command) == 'L_COMMAND':
        return command[1:len(command)-1]
    else:
        return None

def dest(command):
    if commandType(command) == 'C_COMMAND':
        if '=' in command:
            return command[0:command.index('=')]
        else:
            return None
    else:
        return None

def comp(command):
    if commandType(command) == 'C_COMMAND':
        if '=' in command and ';' in command:
            return command[command.index('=') + 1:command.index(';')]
        elif '=' in command and ';' not in command:
            return command[command.index('=') + 1:]
        elif '=' not in command and ';' in command:
            return command[0:command.index(';')]
        else:
            return command
    else:
        return None

def jump(command):
    if commandType(command) == 'C_COMMAND':
        if ';' in command:
            return command[command.index(';') + 1:]
        else:
            return None
    else:
        return None