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
else:
    coder = codewriter.CodeWriter(str(source_split[-1].split('.')[0]))

if len(parsers) > 0:
    #code of many files
    for parser_file in parsers:
        while parser_file.hasMoreCommands():
            parser_file.advance()
            if parser_file.commandType() == 'C_ARITHMETIC':
                coder.writeArithmetic(parser_file.arg1())
            elif parser_file.commandType() == 'C_PUSH':
                coder.writeArithmetic('push', parser_file.arg1(), parser_file.arg2())
            elif parser_file.commandType() == 'C_POP':
                coder.writeArithmetic('pop', parser_file.arg1(), parser_file.arg2())
    coder.close()
else: 
    while files.hasMoreCommands():
        files.advance()
        if files.commandType() == 'C_ARITHMETIC':
            coder.writeArithmetic(files.arg1())
        elif files.commandType() == 'C_PUSH':
            coder.writeArithmetic('push', files.arg1(), files.arg2())
        elif files.commandType() == 'C_POP':
            coder.writeArithmetic('pop', files.arg1(), files.arg2())
    coder.close()