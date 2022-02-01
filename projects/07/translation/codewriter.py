command_sequence1 = [
    '@SP',
    'M=M-1',
    '@M',
    'D=M',
    '@SP',
    'M=M-1',
    '@M',
    'D=D+M',
    '@SP',
    '@M',
    'M=D',
    '@SP',
    'M=M+1'
]
# index 7 is the one to change

command_sequence2 = [
    '@SP',
    'M=M-1',
    '@M',
    'M=0-M',
    '@SP',
    'M=M+1'
]
#index 3 is the one to change

def command_sequence3_get(type, increment):
    command_sequence3 = [
    '@SP',
    'M=M-2',
    '@M',
    'D=M',
    '@SP',
    'M=M+1',
    '@M',
    'D=D-M',
    '@TRUE' + str(increment),
    'D;' + str(type),
    '@SP',
    '@M',
    'M=0',
    '@FINAL' + str(increment),
    '0; JMP',
    '(TRUE' + str(increment) + ')',
    '@SP',
    '@M',
    'M=-1',
    '(FINAL' + str(increment) + ')',
    '@SP',
    'M=M+1'
    ]
    return command_sequence3

def command_sequence4_get(segment, index): #for any
    command_sequence4 = [
        '@' + str(segment),
        'D=M',
        'D=D+' + str(index),
        '@D',
        'D=M',
        '@SP',
        '@M',
        'M=D',
        '@SP',
        'M=M+1'
    ]
    return command_sequence4

def command_sequence5_get(index): #for constant
    command_sequence5 = [
        '@SP',
        '@M',
        'M='+str(index),
        '@SP',
        'M=M+1'
    ]
    return command_sequence5

def command_sequence6_get(index): #temp
    command_sequence6 = [
        'D=5+' + str(index),
        '@D',
        'D=M',
        '@SP',
        '@M',
        'M=D',
        '@SP',
        'M=M+1'
    ]
    return command_sequence6

def command_sequence7_get(index): #pointer
    command_sequence7 = [
        'D=3+' + str(index),
        '@D',
        'D=M',
        '@SP',
        '@M',
        'M=D',
        '@SP',
        'M=M+1'
    ]
    return command_sequence7

class CodeWritter():

    def __init__(self, name):
        self.incrementvar = 0
        self.runningcommands = []
        self.file_name = name + ".asm"
        self.file = open(self.file_name, 'w')

    def writeArithmetic(self, command):
        if command == "add":
            command_sequence1[7] = 'D=D+M'
            for i in command_sequence1:
                self.runningcommands.append(i)
        elif command == "sub":
            command_sequence1[7] = 'D=D-M'
            for i in command_sequence1:
                self.runningcommands.append(i)
        elif command == "neg":
            command_sequence2[3] = 'M=0-M'
            for i in command_sequence2:
                self.runningcommands.append(i)
        elif command == "not":
            command_sequence2[3] = 'M=!M'
            for i in command_sequence2:
                self.runningcommands.append(i)
        elif command == "and":
            command_sequence1[7] = 'D=D&M'
            for i in command_sequence1:
                self.runningcommands.append(i)
        elif command == "or":
            command_sequence1[7] = 'D=D|M'
            for i in command_sequence1:
                self.runningcommands.append(i)
        elif command == "eq":
            for i in command_sequence3_get('JEQ', self.incrementvar):
                self.runningcommands.append(i)
            self.incrementvar += 1
        elif command == "gt":
            for i in command_sequence3_get('JGT', self.incrementvar):
                self.runningcommands.append(i)
            self.incrementvar += 1
        elif command == "lt":
            for i in command_sequence3_get('JLT', self.incrementvar):
                self.runningcommands.append(i)
            self.incrementvar += 1

    def WritePushPop(self, command, segment, index):
        if command == 'push':
            if segment == 'constant':
                for i in command_sequence5_get(index):
                    self.runningcommands.append(i)
                return 0
            elif segment == 'temp':
                for i in command_sequence6_get(index):
                    self.runningcommands.append(i)
                return 0
            elif segment == 'pointer':
                for i in command_sequence7_get(index):
                    self.runningcommands.append(i)
                return 0
            elif segment == 'argument':
                for i in command_sequence4_get('ARG', index):
                    self.runningcommands.append(i)
                return 0
            elif segment == 'local':
                for i in command_sequence4_get('LCL', index):
                    self.runningcommands.append(i)
                return 0
            elif segment == 'this':
                for i in command_sequence4_get('THIS', index):
                    self.runningcommands.append(i)
                return 0
            elif segment == 'that':
                for i in command_sequence4_get('THAT', index):
                    self.runningcommands.append(i)
                return 0
        elif command == 'pop':
            pass

    def close(self):
        self.file.close()