###############################################
#Pre-Issue Buffer
#The pre-issue buffer has 4 entries, each entry can store a single instruction.
#The instructions are sorted in their program order (entry 0 always contains the oldest instruction and entry 3 contains the newest).
###############################################

class PreIssueBuffer(object):
    def __init__(self):
        self.content = [''] * 4     #contents of the Pre Issue Buffer

    def getContent(self, index):
        return self.content[index]

    def setContent(self, content, index):
        self.content[index] = content