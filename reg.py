#========================================================================
# Class RegFile
# Holds the 32 register states that are manipulated upon by writeback.
#========================================================================
class RegFile(object):
	def __init__(self):
		# print 'Testing RegFile().init...'   # TESTPRINT
		self.regFileList = [0] * 32
	
