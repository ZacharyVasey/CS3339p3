#############################################
# Pre MEM
# The pre-mem buffer has two entries.
# Each entry can store an instruction with its address and data (for STUR).
# It is managed as a FIFO queue.
#############################################

class PreMEM(object):
    def __init__(self):
        self.content = [''] * 2    #contents of the pre MEM

    def getContent(self, index):
        return self.content[index]

    def setContent(self, new_content, index):
        self.content[index] = new_content