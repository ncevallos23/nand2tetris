class Parser():

    def __init__(self, address):
        self.address = address
        self.index = -1
        self.commands = []
        self.currentCommand = ""
        self.file = open(self.address, 'r')
        for line in self.file:
            if line == '\n':
                continue
            if line[0:2] == '//':
                continue
            try:
                self.commands.append(line.strip().split('//')[0].split())
            except:
                self.commands.append(line.strip().split())

    
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
        #artehtmeic commands
        if len(self.currentCommand) == 1 and self.currentCommand != 'return':
            return 'C_ARITHMETIC'
        elif self.currentCommand[0] == 'push':
            return 'C_PUSH'
        elif self.currentCommand[0] == 'pop':
            return 'C_POP'
        else:
            return None
        #program flow commands

        #function calling commands

    def arg1(self):
        if self.commandType() == 'C_ARITHMETIC':
            return self.currentCommand[0]
        elif self.commandType() == 'C_PUSH':
            return self.currentCommand[1]
        elif self.commandType() == 'C_POP':
            return self.currentCommand[1]
        else:
            return None


    def arg2(self):
        if self.commandType() == 'C_PUSH':
            return int(self.currentCommand[2])
        elif self.commandType() == 'C_POP':
            return int(self.currentCommand[2])
        else:
            return None


        