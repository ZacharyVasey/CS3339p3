#====================================================================================
# PreMem
# 	Post ALU register. The post-ALU buffer has one entry that can store the 
# 	instruction with the destination register ID and the result of the ALU operation
#====================================================================================

class PreMem(object):
    def __init__(self):
        self.content = [''] * 2    #contents of the pre MEM

    def getContent(self, index):
        return self.content[index]

    def setContent(self, new_content, index):
        self.content[index] = new_content