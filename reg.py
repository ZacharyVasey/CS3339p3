#####################################################################################
# RegFile Class:  	Manages the register file.  Stores 32 register entries.
#####################################################################################
class RegFile(object):
	def __init__(self):
		# print 'Testing RegFile().init...'   # TESTPRINT
		self.regFile = [0] * 32
	#################################################################################
	# printRegFile:		Prints current contents.
	#################################################################################
	def printRegFile(self):
		#print 'Testing printRegFile()...'
		lines = '\nREGISTER FILE\n'
		row = 0
		for outter in range(0, 4):
			lines += 'r' + str(row).zfill(2) + ":\t"
			for inner in range(0, 8):
				lines += str(self.regFile[inner + row]) + "\t"
			lines += "\n"
			row += 8
		print lines

