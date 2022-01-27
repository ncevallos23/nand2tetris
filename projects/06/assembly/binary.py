def getBinary(input):
    current = input
    binary = [0] * 16
    count = 15
    while int(current/2) != 0:
        binary[count] = current % 2
        current = int(current/2)
        count = count - 1
    
    binary[count] = current % 2

    return binary
