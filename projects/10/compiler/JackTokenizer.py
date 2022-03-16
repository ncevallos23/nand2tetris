chars = ['.', ',', '\'', '\"', '<', '=', '>', '(', ')', '{', '}', '[', ']', ';', '~', '+', '-', "/", "*", "&", '|']
keywords = ['class', 'constructor', 'function', 'method', 'field', 'static', 'var', 'int', 'char', 'boolean', 'void', 'true', 'false', 'null', 'this', 'let', 'do', 'if', 'else', 'while', 'return']

class Tokenizer:
    def __init__(self, f):
        self.file = open(f, 'r')
        self.file_path = f
        self.lines = []
        multi = False
        self.tokens = []
        self.string_constants = {} #keys will be in the form of %/s#%
        self.string_count = 0
        self.char_count = 0
        self.token_ind = -1
        self.xmlLines = []
        self.currentToken = ''

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
                    key = '%/s' + str(self.string_count) + '%'
                    self.string_constants += 1
                    self.string_constants[key] = charval
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

        self.file.close()

    def hasMoreTokens(self):
        if self.token_ind < len(self.tokens) - 1:
            return True
        else:
            return False
    
    def advance(self):
        self.token_ind += 1
        self.currentToken = self.tokens[self.token_ind]

    def tokenType(self):
        try:
            if int(self.currentToken) in range(0, 32768):
                return 'integerConstant'
        except:
            if self.currentToken in keywords:
                return 'keyword'
            elif self.currentToken in chars:
                return 'symbol'
            elif self.currentToken[0] == '%':
                return 'stringConstant'
            else:
                return 'indentifier'

    def getToken(self):
        if self.tokenType() == 'stringConstant':
            return self.string_constants[self.currentToken], self.tokenType()
        else:
            return self.currentToken, self.tokenType()
    
    def deAdvance(self, shift):
        self.token_ind -= shift
        self.currentToken = self.tokens[self.token_ind]

#shift = the shift or the char to match, #deBool is to see if function calls deAdvance, #typeBool is to see if we get char or shift, true means shfit
    def lookAhead(self, shift, deBool, typeBool):
        commands = []
        commands.append(self.getToken())
        if typeBool:
            for time in range(0, shift):
                self.advance()
                commands.append(self.getToken())
            if deBool:
                self.deAdvance(shift)
            return commands
        else:
            count = 0
            while(self.getToken()[0] != shift):
                self.advance()
                count+=1
                commands.append(self.getToken())
            if deBool:
                self.deAdvance(count)
            commands.append(self.getToken())
            return commands
