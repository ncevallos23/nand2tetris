from assembly import code, parser, binary

file = parser.initalize()
index = 0

commands_bin = []

for command in file:
    type = parser.commandType(command)
    if type == 'A_COMMAND' or type == 'L_COMMAND':
        address = parser.symbol(command)
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

for com_bin in commands_bin:
    for bin in com_bin:
        print(bin, end="")
    print("")