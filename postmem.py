#############################################
# Post MEM
#
#############################################

class PostMEM(object):
    def __init__(self):
        self.content = ''     #contents of the post MEM

    def getContent(self):
        return self.content

    def setContent(self, new_content):
        self.content = new_content