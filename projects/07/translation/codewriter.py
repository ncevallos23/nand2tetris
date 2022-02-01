class CodeWritter():

    def __init__(self, name):
        self.file_name = name + ".asm"
        self.file = open(self.file_name, 'w')

    def writeArithmetic(self, command):
        if command == "add":
            

    def WritePushPop(self, command, segment, index):
        pass

    def close(self):
        self.file.close()