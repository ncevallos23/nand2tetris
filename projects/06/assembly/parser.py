import sys

file = sys.argv[1]

def initalize():
    f = open(file, 'r')
    lines = []
    for line in f:
        lines.append(line)
    
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
        return command[1:len(command)]
    else:
        return None

def dest(command):
    if commandType(command) == 'C_COMMAND':
        return command[10:13]
    else:
        return None

def comp(command):
    if commandType(command) == 'C_COMMAND':
        return command[3:10]
    else:
        return None

def jump(command):
    if commandType(command) == 'C_COMMAND':
        return command[13:]
    else:
        return None