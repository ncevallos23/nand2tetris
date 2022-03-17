import sys
import JackTokenizer
import CompilationEngine
import os
#this is my main function

recepticle = sys.argv[1].strip()
folder = False

tokenizers = []

if ".jack" not in recepticle:
    folder = True
    files = os.listdir(recepticle)
    for file in files:
        if ".jack" in file:
            tokenizers.append(JackTokenizer.Tokenizer(recepticle+'/'+file))
        else:
            pass
else:
    tokenizers = JackTokenizer.Tokenizer(recepticle)

if type(tokenizers) is list:
    #we know its a folder
    for tokenizer in tokenizers:
        #while(tokenizer.hasMoreTokens()):
        #    tokenizer.advance()
        #    token, tType = tokenizer.getToken()
        #    print("Token: " + token + " of type " + tType)
        tokenizer.advance()
        current_comp = CompilationEngine.CompilationEngine(tokenizer, 'a')
        current_comp.CompileClass()
else:
    #while(tokenizers.hasMoreTokens()):
    #    tokenizers.advance()
    #    token, tType = tokenizers.getToken()
    #    print("Token: " + token + " of type " + tType)
    tokenizers.advance()
    current_comp = CompilationEngine.CompilationEngine(tokenizers, 'a')
    current_comp.CompileClass()



    