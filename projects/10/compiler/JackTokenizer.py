class Tokenizer:
    def __init__(self, f):
        self.file = open(f, 'r')

        self.lines = []
        multi = False
        chars = ['.', ',', '\'', '\"', '<', '=', '>', '(', ')', '{', '}', '[', ']', ';', '~', '+', '-', "/", "*", "&", '|']
        self.tokens = []
        self.string_constants = {} #keys will be in the form of %/s#%
        self.char_constants = {} #keys will be in the form of %/c#%
        self.string_count = 0
        self.char_count = 0

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
                self.lines.append(line.strip().split('//')[0].strip())
            except:
                self.lines.append(line.strip())
            try:
                self.lines.remove('')
            except:
                pass

        for bline in self.lines:
            line_string = list(bline)
            if line_string[0:2] == list('if'):
                if line_string[2] == '(':
                    line_string.insert(2, ' ')
                if line_string[-1] == '{' and line_string[-2] == ')':
                    line_string.insert(len(line_string)-1, ' ')
            if line_string[0:5] == list('while'):
                if line_string[5] == '(':
                    line_string.insert(5, ' ')
                if line_string[-1] == '{' and line_string[-2] == ')':
                    line_string.insert(len(line_string)-1, ' ')
            #get string constants
            inString = False
            inChar = False
            start_index = 0
            end_index = 0
            index = 0
            stringval = ''
            charval = ''
            key = ''
            for char in line_string:
                if char == '\"' and not inString:
                    inString = True
                    index += 1
                    start_index = index
                    continue
                if char == '\"' and inString:
                    inString = False
                    end_index = index
                    index += 1
                    key = '%/s'+str(self.string_count)+'%'
                    self.string_count += 1
                    stringval = ''
                    for i in range(start_index, end_index):
                        stringval += line_string[i]
                        line_string[i] = ' '
                    self.string_constants[key] = stringval
                    line_string[start_index] = key
                    continue
                if char == '\'' and not inChar:
                    inChar = True
                    index += 1
                    charval = line_string[index]
                    continue
                if char == '\'' and inChar:
                    inChar = False
                    key = '%/c' + str(self.char_count) + '%'
                    self.char_count += 1
                    self.char_constants[key] = charval
                    line_string[index - 1] = key
                    index += 1
                    continue
                index += 1
            
            index = 0
            for char in line_string:
                if char in chars:
                    if line_string[index-1] == ' ':
                        index += 1
                        line_string.insert(index, ' ')
                        continue
                    line_string.insert(index, ' ')
                    line_string.insert(index+2, ' ')
                index += 1

            newLine = ''
            for char in line_string:
                newLine += char

            for token in newLine.split():
                self.tokens.append(token)

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