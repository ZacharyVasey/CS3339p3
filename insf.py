#========================================================================
# Class IF
#  Manages the instruction fetch stage.
#========================================================================
class IF(object):
	def __init__(self, bd):
		self.binData = bd
	def run(self):
		print
		# print '\nHere are your opcode strings...'
		for ind, opc in enumerate(self.binData.opCodeStr):
			if opc == 'BREAK':
				break
			else:
				# print opc, '  ',
				pc = self.binData.memLines[ind]
				# GRAB CURRENT PC FOR INST
				print 'Current PC:   ', pc
				print '\tpc:  ', bin(pc)
				
				# GRAB BYTE OFFSET
				boffMask = 0x7
				boff = boffMask & pc
				print '\tboff: ', boff
				
				# GRAB TAG
				tag = pc >> 5
				print '\ttag:  ', tag

				# GRAB SET INDEX FOR EACH INS
				setIndex = pc >> 3
				setMask = 0x3
				setIndex = setMask & setIndex
				print '\tsetIndex: ', setIndex
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				