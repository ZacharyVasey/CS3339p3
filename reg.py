#========================================================================
# Class RegFile
# Holds the 32 register states that are manipulated upon by writeback.
#========================================================================
class RegFile(object):
	def __init__(self):
		# print 'Testing RegFile().init...'   # TESTPRINT
		self.regFile = [0] * 32

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

