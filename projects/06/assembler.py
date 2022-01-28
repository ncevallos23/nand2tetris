from assembly import code, parser, binary, SymbolTable

file = parser.initalize()
index = -1
offset = 0

commands_bin = []
new_address = 16

for command in file:
    index += 1
    type = parser.commandType(command)
    if type == 'L_COMMAND':
        symbol = parser.symbol(command)
        if not SymbolTable.contains(symbol):
            SymbolTable.addEntry(symbol, index-offset)
            offset+=1
    else:
        pass

for command in file:
    type = parser.commandType(command)
    if type == 'A_COMMAND':
        symbol = parser.symbol(command)
        if not SymbolTable.contains(symbol) and not symbol.isnumeric():
            SymbolTable.addEntry(symbol, new_address)
            new_address+= 1
    else:
        pass

for command in file:
    type = parser.commandType(command)
    if type == 'A_COMMAND':
        address = parser.symbol(command)
        if SymbolTable.contains(address):
            commands_bin.append(binary.getBinary(SymbolTable.getAddress(address)))
        else:
            commands_bin.append(binary.getBinary(int(address)))
    elif type == 'C_COMMAND':
        dest_text = parser.dest(command)
        comp_text = parser.comp(command)
        jump_text = parser.jump(command)
        dest_bin = code.dest(dest_text)
        comp_bin = code.comp(comp_text)
        jump_bin = code.jump(jump_text)
        start = [1, 1, 1]
        commands_bin.append(start + comp_bin + dest_bin + jump_bin)
    else:
        continue

commands_str = []

for com_bin in commands_bin:
    string = ""
    for bin in com_bin:
        print(bin, end="")
        string = string + str(bin)
    commands_str.append(string)
    print("")

name = input("name>")
final = open(name, 'w')
for i in commands_str:
    final.write(i + "\n")

final.close()
