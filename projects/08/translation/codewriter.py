command_sequence1 = [ # index 7 is the one to change
    '@2',
    'D=A',
    '@SP',
    'M=M-D',
    'A=M',
    'D=M',
    '@SP',
    'M=M+1',
    'A=M',
    'D=D+M',
    '@SP',
    'A=M-1',
    'M=D',
    '@SP',
    'A=M',
    'M=0'
]

command_sequence2 = [ #index 3 is the one to change
    '@SP',
    'M=M-1',
    'A=M',
    'M=0-M',
    '@SP',
    'M=M+1'
]

def command_sequence3_get(type, increment):
    command_sequence3 = [
    '@2',
    'D=A',
    '@SP',
    'M=M-D',
    'A=M',
    'D=M',
    '@SP',
    'M=M+1',
    'A=M',
    'D=D-M',
    '@TRUE' + str(increment),
    'D;' + str(type),
    '@SP',
    'A=M',
    'M=0',
    'A=A-1',
    'M=0',
    '@FINAL' + str(increment),
    '0; JEQ',
    '(TRUE' + str(increment) + ')',
    '@SP',
    'A=M-1',
    'M=-1',
    'A=A+1',
    'M=0',
    '(FINAL' + str(increment) + ')'
    ]
    return command_sequence3

def command_sequence4_get(segment, index):
    command_sequence4 = [
        '@' + str(segment),
        'D=M',
        '@' + str(index),
        'D=D+A',
        'A=D',
        'D=M',
        '@SP',
        'A=M',
        'M=D',
        '@SP',
        'M=M+1'
    ]
    return command_sequence4

def command_sequence5_get(index): #for constant
    command_sequence5 = [
        '@' + str(index),
        'D=A',
        '@SP',
        'A=M',
        'M=D',
        '@SP',
        'M=M+1'
    ]
    return command_sequence5

def command_sequence6_get(index): #temp
    command_sequence6 = [
        '@5',
        'D=A',
        '@' + str(index),
        'D=D+A',
        'A=D',
        'D=M',
        '@SP',
        'A=M',
        'M=D',
        '@SP',
        'M=M+1'
    ]
    return command_sequence6

def command_sequence7_get(index): #pointer
    command_sequence7 = [
        '@3',
        'D=A',
        '@' + str(index),
        'D=D+A',
        'A=D',
        'D=M',
        '@SP',
        'A=M',
        'M=D',
        '@SP',
        'M=M+1'
    ]
    return command_sequence7

def command_sequence8_get(index, file): #static
    command_sequence8 = [
        '@' + str(file) + '.' + str(index),
        'D=M',
        '@SP',
        'A=M',
        'M=D',
        '@SP',
        'M=M+1'
    ]
    return command_sequence8

def command_sequence9_get(segment, index): #for any pop
    command_sequence9 = [
        '@' + str(segment),
        'D=M',
        '@' + str(index),
        'D=D+A',
        '@13',
        'M=D',
        '@SP',
        'M=M-1',
        'A=M',
        'D=M',
        'M=0',
        '@13',
        'A=M',
        'M=D'
    ]
    return command_sequence9

def command_sequence10_get(index): #temp
    command_sequence10 = [
        '@5',
        'D=A',
        '@' + str(index),
        'D=D+A',
        '@13',
        'M=D',
        '@SP',
        'M=M-1',
        'A=M',
        'D=M',
        'M=0',
        '@13',
        'A=M',
        'M=D'
    ]
    return command_sequence10

def command_sequence11_get(index): #pointer
    command_sequence11 = [
        '@3',
        'D=A',
        '@' + str(index),
        'D=D+A',
        '@13',
        'M=D',
        '@SP',
        'M=M-1',
        'A=M',
        'D=M',
        'M=0',
        '@13',
        'A=M',
        'M=D'
    ]
    return command_sequence11

def command_sequence12_get(index, file): #static
    command_sequence12 = [
        '@SP',
        'M=M-1',
        'A=M',
        'D=M',
        'M=0',
        '@' + str(file) + '.' + str(index),
        'M=D'
    ]
    return command_sequence12

def command_sequence13_get(label):
    command_sequence13 = [
        '@' + str(label),
        '0;JMP'
    ]
    return command_sequence13

def command_sequence14_get(label):
    command_sequence14 = [
        '@SP',
        'M=M-1',
        'A=M',
        'D=M',
        'M=0',
        '@' + str(label),
        'D;JNE'
    ]
    return command_sequence14

def command_sequence15_get(functionName, numArgs, ranum): #call code
    command_sequence15 = [
        '@returnaddy' + str(ranum),
        'D=A',
        '@SP',
        'A=M',
        'M=D',
        '@SP',
        'M=M+1',
        '@LCL',
        'D=M',
        '@SP',
        'A=M',
        'M=D',
        '@SP',
        'M=M+1',
        '@ARG',
        'D=M',
        '@SP',
        'A=M',
        'M=D',
        '@SP',
        'M=M+1',
        '@THAT',
        'D=M',
        '@SP',
        'A=M',
        'M=D',
        '@SP',
        'M=M+1',
        '@THIS',
        'D=M',
        '@SP',
        'A=M',
        'M=D',
        '@SP',
        'M=M+1',
        '@SP',
        'D=M',
        '@' + str(numArgs),
        'D=D-A',
        '@5',
        'D=D-A',
        '@ARG',
        'M=D',
        '@SP',
        'D=M',
        '@LCL',
        'M=D',
        '@' + str(functionName),
        '0; JMP',
        '(returnaddy' + str(ranum) + ')'
    ]
    return command_sequence15

def command_sequence16_get(functionName, numLocals): #function code
    command_sequence16 = [
        '(' + str(functionName) + ')',
    ]
    for time in range(0, numLocals):
        command_sequence16 = command_sequence16 + command_sequence5_get(0)

    return command_sequence16

def command_sequence17_get(): #return code
    command_sequence17 = [
        '@LCL',
        'D=M',
        '@13', #this is now frame
        'M=D',
        '@5',
        'D=D-A',
        'A=D',
        'D=M',
        '@14', #return address
        'M=D',
        '@SP',
        'A=M-1',
        'D=M',
        '@ARG',
        'A=M',
        'M=D',
        '@ARG',
        'D=M',
        '@SP',
        'M=D+1',
        '@13',
        'D=M',
        '@1',
        'A=D-A',
        'D=M',
        '@THAT',
        'M=D',
        '@13',
        'D=M',
        '@2',
        'A=D-A',
        'D=M',
        '@THIS',
        'M=D',
        '@13',
        'D=M',
        '@3',
        'A=D-A',
        'D=M',
        '@ARG',
        'M=D',
        '@13',
        'D=M',
        '@4',
        'A=D-A',
        'D=M',
        '@LCL',
        'M=D',
        '@14',
        'A=M',
        '0;JMP'
    ]
    return command_sequence17

def command_sequence18_get():
    command_sequence18 = [
        '@256',
        'D=A',
        '@SP',
        'M=D'
        ]
    return command_sequence18 + command_sequence15_get('Sys.init', 0, 0)

class CodeWriter():

    def __init__(self, name):
        self.incrementvar = 0
        self.returnvar = 1
        self.runningcommands = []
        self.file_name = name + ".asm"
        self.file = open(self.file_name, 'w')

    def writeArithmetic(self, command):
        if command == "add":
            command_sequence1[9] = 'D=D+M'
            for i in command_sequence1:
                self.runningcommands.append(i)
        elif command == "sub":
            command_sequence1[9] = 'D=D-M'
            for i in command_sequence1:
                self.runningcommands.append(i)
        elif command == "neg":
            command_sequence2[3] = 'M=-M'
            for i in command_sequence2:
                self.runningcommands.append(i)
        elif command == "not":
            command_sequence2[3] = 'M=!M'
            for i in command_sequence2:
                self.runningcommands.append(i)
        elif command == "and":
            command_sequence1[9] = 'D=D&M'
            for i in command_sequence1:
                self.runningcommands.append(i)
        elif command == "or":
            command_sequence1[9] = 'D=D|M'
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

    def writePushPop(self, command, segment, index, file_name):
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
            elif segment == 'static':
                for i in command_sequence8_get(index, file_name):
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
            if segment == 'temp':
                for i in command_sequence10_get(index):
                    self.runningcommands.append(i)
                return 0
            elif segment == 'pointer':
                for i in command_sequence11_get(index):
                    self.runningcommands.append(i)
                return 0
            elif segment == 'static':
                for i in command_sequence12_get(index, file_name):
                    self.runningcommands.append(i)
                return 0
            elif segment == 'argument':
                for i in command_sequence9_get('ARG', index):
                    self.runningcommands.append(i)
                return 0
            elif segment == 'local':
                for i in command_sequence9_get('LCL', index):
                    self.runningcommands.append(i)
                return 0
            elif segment == 'this':
                for i in command_sequence9_get('THIS', index):
                    self.runningcommands.append(i)
                return 0
            elif segment == 'that':
                for i in command_sequence9_get('THAT', index):
                    self.runningcommands.append(i)
                return 0

    def writeLabel(self, label):
        self.runningcommands.append("(" + label + ")")

    def writeGoto(self, label):
        for i in command_sequence13_get(label):
            self.runningcommands.append(i)

    def writeIf(self, label):
        for i in command_sequence14_get(label):
            self.runningcommands.append(i)

    def writeCall(self, functionName, numArgs):
        for i in command_sequence15_get(functionName, numArgs, self.returnvar):
            self.runningcommands.append(i)
        self.returnvar += 1

    def writeReturn(self):
        for i in command_sequence17_get():
            self.runningcommands.append(i)
    
    def writeFunction(self, functionName, numLocals):
        for i in command_sequence16_get(functionName, numLocals):
            self.runningcommands.append(i)

    def writeInit(self):
        for i in command_sequence18_get():
            self.runningcommands.append(i)

    def close(self):
        for command in self.runningcommands:
            self.file.write(command + '\n')
        self.file.close()