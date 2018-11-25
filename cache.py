#========================================================================
# Class Cache
#  Aint nothin counterfeit here.
#========================================================================
import copy
class Cache(object):
	def __init__(self):
		self.ch = []
		# Initialize empty cache.  ch -> 4 sets -> 2 blocks
		bl = [0, False, False, 0, 0, 0]
		st = []
		for x in range(0, 4):
			for y in range(0, 2):
				st = copy.deepcopy([])
				st.append(copy.deepcopy(bl))
				st.append(copy.deepcopy(bl))
			self.ch.append(copy.deepcopy(st))
	
	#====================================================================
	#   testPrint function:  prints state of cache at a moment.
	#====================================================================
	def testPrint(self):
		print('\nHere is your current cache:')
		for num, set in enumerate(self.ch):
			print('Set ' + str(num))
			for block in set:
				print(block)
				
			
			