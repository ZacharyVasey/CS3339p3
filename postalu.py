#====================================================================================
# Class PostALU
# 	Post ALU register. The post-ALU buffer has one entry that can store the 
# 	instruction with the destination register ID and the result of the ALU operation
#====================================================================================
class PostALU(object):
    
    def __init__(self):
        self.regInd = None 
        self.regVal = None
  	
  	def setContent(ri, rv):
  		self.regInd = ri
  		self.regVal = rv

  	def printContent:
  		print 'PostALU:\n' + 'regInd: ' + str(self.regIndex) + '\nregVal:' + str(self.regVal)