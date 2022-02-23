class Parser():

    def __init__(self, address, file_name):
        self.address = address
        self.index = -1
        self.commands = []
        self.currentCommand = ""
        self.file = open(self.address, 'r')
        self.file_name = file_name
        for line in self.file:
            if line == '\n':
                continue
            if line[0:2] == '//':
                continue
            try:
                self.commands.append(line.strip().split('//')[0].split())
            except:
                self.commands.append(line.strip().split())

    def getName(self):
        return self.file_name

    def hasMoreCommands(self):
        if self.index < len(self.commands) - 1:
            return True
        else:
            return False

    def advance(self):
        if self.hasMoreCommands():
            self.index += 1
            self.currentCommand = self.commands[self.index]

    def commandType(self):
        if self.currentCommand[0] == 'return':
            return 'C_RETURN'
        elif self.currentCommand[0] == 'push':
            return 'C_PUSH'
        elif self.currentCommand[0] == 'pop':
            return 'C_POP'
        elif self.currentCommand[0] == 'label':
            return 'C_LABEL'
        elif self.currentCommand[0] == 'goto':
            return 'C_GOTO'
        elif self.currentCommand[0] == 'if-goto':
            return 'C_IF'
        elif self.currentCommand[0] == 'function':
            return 'C_FUNCTION'
        elif self.currentCommand[0] == 'call':
            return 'C_CALL'
        else:
            return 'C_ARITHMETIC'

    def arg1(self):
        if self.commandType() == 'C_ARITHMETIC' or self.commandType() == 'C_RETURN':
            return self.currentCommand[0]
        else:
            return self.currentCommand[1]

    def arg2(self):
        if self.commandType() == 'C_PUSH':
            return int(self.currentCommand[2])
        elif self.commandType() == 'C_POP':
            return int(self.currentCommand[2])
        elif self.commandType() == 'C_FUNCTION':
            return int(self.currentCommand[2])
        elif self.commandType() == 'C_CALL':
            return int(self.currentCommand[2])

        