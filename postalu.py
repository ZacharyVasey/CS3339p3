#====================================================================================
# PostALU
# 	Post ALU register. The post-ALU buffer has one entry that can store the 
# 	instruction with the destination register ID and the result of the ALU operation
#====================================================================================
class PostAlu(object):
    
	def __init__(self):
		self.regInd = None 
		self.regVal = None
  	
	def setContent(self, ri, rv):
		self.regInd = ri
		self.regVal = rv

	def printContent(self):
		print 'PostAlu:  ' + 'regInd, ' + str(self.regInd) + '   ' + 'regVal, ' \
		+ str(self.regVal)