#####################################################################################
# PostAlu Class:  	manages the Post-ALU buffer.  Stores only one entry at a time:
#					a register index, and a register value.
#####################################################################################
class PostAlu(object):
	def __init__(self):
		self.regInd = None 
		self.regVal = None
	#################################################################################
	# setContent:	Takes a register index and register value.  Stores them to self.
	#################################################################################
	def setContent(self, ri, rv):
		self.regInd = ri
		self.regVal = rv
	#################################################################################
	# printContent:		Prints current content.
	#################################################################################
	def printContent(self):
		print 'PostAlu:  ' + 'regInd, ' + str(self.regInd) + '   ' + 'regVal, ' \
		+ str(self.regVal)