#========================================================================
# Class PreALU()
# Post ALU register.
# The pre-ALU buffer has two entries.
# Each entry can store an instruction with its operands.
# The buffer is managed as a FIFO queue
#========================================================================
class PreALU(object):
    def __init__(self):
        self.content = [''] * 2    #contents of the pre ALU

    def getContent(self, index):
        return self.content[index]

    def setContent(self, new_content, index):
        self.content[index] = new_content