class Tokenizer:
    def __init__(self, file):
        self.file = open(file, 'r')
        #process the commands here
        self.index = 0
        self.currentCommand = ''

    def hasMoreTokens(self):
        if self.index < len(self.file) - 1:
            return True
        else:
            return False
    
    def advance(self):
        self.index += 1
        self.currentCommand = self.file[self.index]

    def tokenType(self):
        pass

    def keyWord(self):
        pass

    def symbol(self):
        pass

    def identifier(self):
        pass

    def intVal(self):
        pass

    def stringVal(self):
        pass