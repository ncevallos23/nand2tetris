import JackTokenizer
import sys

keywordSub = ['constructor', 'function', 'method']
keywordClassVarDec = ['field', 'static']
keywordType = ['int', 'char', 'bool', 'void']

def splitList(l, seperator):
    spliced = list()
    for time in range(0, l.count(seperator)):
        new = list()
        count = 1
        for val in l:
                new.append(val)
                count+=1
                if val == seperator:
                    del l[0:count]
                    break
        spliced.append(new)
    return

class CompilationEngine:
    def __init__(self, token_in, file_out):
        self.tokenizer_in = token_in #this is a JackTokenizer class
        self.output = []
        self.out_file = file_out
    
    def CompileClass(self):
        self.output.append('<class>')
        class_check = self.tokenizer_in.lookAhead(2, False, True)
        if class_check[1][1] == 'identifier' and class_check[2][0] == '{':
            self.output.append('<'+class_check[0][1]+'>'+' '+class_check[0][0]+' '+'</'+class_check[0][1]+'>')
            self.output.append('<'+class_check[1][1]+'>'+' '+class_check[1][0]+' '+'</'+class_check[1][1]+'>')
            self.output.append('<'+class_check[2][1]+'>'+' '+class_check[2][0]+' '+'</'+class_check[2][1]+'>')
        else:
            print("error with class declaration")
            sys.exit()
        while(self.tokenizer_in.hasMoreTokens()):
            self.tokenizer_in.advance()
            current = self.tokenizer_in.getToken()
            if current[0] in keywordClassVarDec:
                self.CompileClassVarDec()
            elif current[0] in keywordSub:
                self.CompileSubroutine()
            else:
                #print(self.output)
                print("error with class var dec or subroutine dec")
                sys.exit()
        self.output.append('</class>')

    def CompileClassVarDec(self):
        self.output.append('<classVarDec>')
        var_check = self.tokenizer_in.lookAhead(';', False, False)
        for token in var_check:
            self.output.append('<'+token[1]+'>'+' '+token[0]+' '+'</'+token[1]+'>')
        self.output.append('</classVarDec>')

    def CompileSubroutine(self):
        self.output.append('<subroutineDec>')
        subRoutine_check = self.tokenizer_in.lookAhead(2, False, True)
        if subRoutine_check[0][0] in keywordSub and subRoutine_check[2][1] == 'identifier':
            self.output.append('<'+subRoutine_check[0][1]+'>'+' '+subRoutine_check[0][0]+' '+'</'+subRoutine_check[0][1]+'>')
            self.output.append('<'+subRoutine_check[1][1]+'>'+' '+subRoutine_check[1][0]+' '+'</'+subRoutine_check[1][1]+'>')
            self.output.append('<'+subRoutine_check[2][1]+'>'+' '+subRoutine_check[2][0]+' '+'</'+subRoutine_check[2][1]+'>')
        else:
            print('error with subroutine declartation')
            sys.exit()
        
        self.compileParameterList()
        self.compileStatements()

        self.output.append('</subroutineDec>')

    def compileParameterList(self):
        self.tokenizer_in.advance() #we should be at the '('
        first = self.tokenizer_in.getToken()
        self.output.append('<'+first[1]+'> ' + first[0] + ' </'+first[1]+'>')
        self.tokenizer_in.advance()
        parameter_check = self.tokenizer_in.lookAhead(')', False, False)
        self.output.append('<parameterList>')
        if parameter_check[-1][0] == ')' and self.tokenizer_in.lookAhead(1, True, True)[1][0] == '{':
            for para in parameter_check:
                self.output.append('<'+para[1]+'>'+' '+para[0]+' '+'</'+para[1]+'>')
            last = self.output.pop()
        else:
            print("error in Parameter List dec")
            sys.exit()
        self.output.append('</parameterList>')
        self.output.append(last)

    def compileStatements(self, callLocation): #compileParamenterList left the current token at the '{'
        #Documentation for callLocation
        #callLocation = 0: called from inside a CompileSubroutine
        #callLocation = 1: called from inisde something else
        if callLocation == 0:
            self.output.append('<subroutineBody>')
            statements_check = self.tokenizer_in.lookAheadList(keywordSub, True, True)
            self.output.append('<'+statements_check[0][1]+'> '+statements_check[0][0]+' </'+statements_check[0][1]+'>')
            while(self.tokenizer_in.getToken()[0] != '}' and self.tokenizer_in.lookAhead(1, True, True)[1][0] not in keywordSub):
                self.tokenizer_in.advance()
                if self.tokenizer_in.getToken()[0] == 'var':
                    self.compileVarDec()
                elif self.tokenizer_in.getToken()[0] == 'if':
                    self.compileIf()
                elif self.tokenizer_in.getToken()[0] == 'do':
                    self.compileDo()
                elif self.tokenizer_in.getToken()[0] == 'let':
                    self.compileLet()
                elif self.tokenizer_in.getToken()[0] == 'while':
                    self.compileWhile()
                elif self.tokenizer_in.getToken()[0] == 'return':
                    self.compileReturn()
                else:
                    print("error in statements dec")
                    sys.exit()

            self.output.append('<'+statements_check[-1][1]+'> '+statements_check[-1][0]+' </'+statements_check[-1][1]+'>')
            self.output.append('</subroutineBody>')
        else:
            pass
    
    def compileVarDec(self):
        self.output.append('<varDec>')
        var_check = self.tokenizer_in.lookAhead(';', False, False)
        for token in var_check:
            self.output.append('<'+token[1]+'>'+' '+token[0]+' '+'</'+token[1]+'>')
        self.output.append('</VarDec>')

    def compileDo(self):
        pass

    def compileLet(self):
        pass

    def compileWhile(self):
        pass

    def compileReturn(self):
        pass

    def compileIf(self):
        pass

    def CompileExpression(self):
        pass

    def CompileTerm(self):
        pass

    def CompileExpressionList(self):
        pass