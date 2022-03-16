import JackTokenizer
import sys

keywordSub = ['constructor', 'function', 'method']
keywordClassVarDec = ['field', 'static']

class CompilationEngine:
    def __init__(self, token_in, file_out):
        self.tokenizer_in = token_in #this is a JackTokenizer class
        self.output = []
        self.out_file = file_out
    
    def CompileClass(self):
        self.output.append('<class>')
        class_check = self.tokenizer_in.lookAhead(2, True)
        if class_check[1][1] == 'identifier' and class_check[2][0] == '{':
            self.output.append('<'+class_check[0][1]+'>'+' '+class_check[0][0]+' '+'</'+class_check[0][1]+'>')
            self.output.append('<'+class_check[1][1]+'>'+' '+class_check[1][0]+' '+'</'+class_check[1][1]+'>')
            self.output.append('<'+class_check[2][1]+'>'+' '+class_check[2][0]+' '+'</'+class_check[2][1]+'>')
        else:
            print("error with class declaration")
            print(class_check[0][0] + ' ' + class_check[1][0] + ' ' + class_check[2][0])
            sys.exit()
        while(self.tokenizer_in.hasMoreTokens()):
            self.tokenizer_in.advance()
            current = self.tokenizer_in.getToken()
            if current[0] in keywordClassVarDec:
                self.CompileClassVarDec()
            elif current[0] in keywordSub:
                self.CompileSubroutine()
            else:
                print("error with class var dec or subroutine dec")
                sys.exit()
        self.output.append('</class>')

    def CompileClassVarDec(self):
        pass

    def CompileSubroutine(self):
        pass

    def compileParameterList(self):
        pass

    def compileVarDec(self):
        pass

    def compileStatements(self):
        pass

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