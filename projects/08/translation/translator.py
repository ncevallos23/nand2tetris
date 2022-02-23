import os

import codewriter, parser

source = input("prompt> ")
files = []
folder = False

parsers = []

source_split = source.split('/')

if ".vm" not in source:
    folder = True
    files = os.listdir(source)
    for file in files:
        if ".vm" in file:
            parsers.append(parser.Parser(address = source + "/" + file))
        else:
            pass
else:
    files = parser.Parser(source)

if len(parsers) > 0:
    coder = codewriter.CodeWriter(str(source_split[-1]))
    #coder.writeInit()
    for parser_file in parsers:
        while parser_file.hasMoreCommands():
            parser_file.advance()
            if parser_file.commandType() == 'C_ARITHMETIC':
                coder.writeArithmetic(parser_file.arg1())
            elif parser_file.commandType() == 'C_PUSH':
                coder.writePushPop('push', parser_file.arg1(), parser_file.arg2())
            elif parser_file.commandType() == 'C_POP':
                coder.writePushPop('pop', parser_file.arg1(), parser_file.arg2())
            elif parser_file.commandType() == 'C_LABEL':
                coder.writeLabel(parser_file.arg1())
            elif parser_file.commandType() == 'C_GOTO':
                coder.writeGoto(parser_file.arg1())
            elif parser_file.commandType() == 'C_IF':
                coder.writeIf(parser_file.arg1())
            elif parser_file.commandType() == 'C_FUNCTION':
                coder.writeFunction(parser_file.arg1(), parser_file.arg2())
            elif parser_file.commandType() == 'C_CALL':
                coder.writeCall(parser_file.arg1(), parser_file.arg2())
            elif parser_file.commandType() == 'C_RETURN':
                coder.writeReturn()
            else:
                print("no command detected")
    coder.close()
else:
    coder = codewriter.CodeWriter(str(source_split[-1].split('.')[0]))
    #coder.writeInit()
    while files.hasMoreCommands():
        files.advance()
        if files.commandType() == 'C_ARITHMETIC':
            coder.writeArithmetic(files.arg1())
        elif files.commandType() == 'C_PUSH':
            coder.writePushPop('push', files.arg1(), files.arg2())
        elif files.commandType() == 'C_POP':
            coder.writePushPop('pop', files.arg1(), files.arg2())
        elif files.commandType() == 'C_LABEL':
            coder.writeLabel(files.arg1())
        elif files.commandType() == 'C_GOTO':
            coder.writeGoto(files.arg1())
        elif files.commandType() == 'C_IF':
            coder.writeIf(files.arg1())
        elif files.commandType() == 'C_FUNCTION':
            coder.writeFunction(files.arg1(), files.arg2())
        elif files.commandType() == 'C_CALL':
            coder.writeCall(files.arg1(), files.arg2())
        elif files.commandType() == 'C_RETURN':
            coder.writeReturn()
        else:
            print("no command detected")
    coder.close()