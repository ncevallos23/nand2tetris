import re

class Tokenizer:
    def __init__(self, file):
        self.file = open(file, 'r')
        multi = False
        for line in self.file:
            if '/**' in line and '*/' in line:
                continue
            if '/**' in line:
                multi = True
                continue
            if '*/' in line:
                multi = False
                continue
            if multi:
                continue
            if line == '\n':
                continue
            if line[0:2] == '//':
                continue
            try:
                self.lines.append(line.strip().split('//')[0])
            except:
                self.lines.append(line.strip())
        self.lines = []
        self.index = 0
        self.currentToken = ''
        self.tokens = []
        for line in self.lines:
            pass#TODO


    def hasMoreTokens(self):
        if self.index < len(self.tokens) - 1:
            return True
        else:
            return False
    
    def advance(self):
        self.index += 1
        self.currentToken = self.tokens[self.index]

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