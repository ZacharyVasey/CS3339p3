#========================================================================
# Class PostALU()
# Post ALU register.
# The post-ALU buffer has one entry that can store the instruction with the destination register ID and the result of the ALU operation
#========================================================================
class PostALU(object):
    def __init__(self):
        self.content = ''     #contents of the post ALU

    def getContent(self):
        return self.content

    def setContent(self, new_content):
        self.content = new_content