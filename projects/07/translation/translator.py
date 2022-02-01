import os

import codewriter, parser

source = input("prompt> ")
files = []
folder = False

parsers = []

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
    #code of many files
    for parser_file in parsers:
        while parser_file.hasMoreCommands():
            #run through them
            pass
else: 
    #code for only one file
    pass

