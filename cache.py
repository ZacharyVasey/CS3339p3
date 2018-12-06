#========================================================================
# Class Cache
#  Aint nothin counterfeit here.
#========================================================================
import copy
class Cache(object):
	def __init__(self):
		self.setIndexMask = 0x18
		self.start = 96
		self.ch = []
		# Initialize empty cache.  ch -> 4 sets -> 2 blocks
		bl = [0, 0, 0, 0, 0, 0]
		st = []
		for x in range(0, 4):
			for y in range(0, 2):
				st = copy.deepcopy([])
				st.append(copy.deepcopy(bl))
				st.append(copy.deepcopy(bl))
			self.ch.append(copy.deepcopy(st))

	def printCache(self):
		lines = "\nCACHE\t[V, D, T, W, W, LRU]"
		for num, set in enumerate(self.ch):
			lines += '\nSet' + str(num) + '\t'
			for block in set:
				lines += '\n\t' + str(block)
		print lines


	def getBlockOffset(self, pc):
		if pc % 8 == 0:
			return 0
		return 1

	def getSetIndex(self, pc):
		setIndex = None
		#print "SetIndexMask:", self.setIndexMask, "~", str(bin(self.setIndexMask))
		setIndex = self.setIndexMask & pc
		#print "SetIndexMask & PC", setIndex
		setIndex = setIndex >> 3
		#print "SetIndex >> 3:  ", setIndex
		return setIndex

	def getTag(self, pc):
		return pc >> 5


	def isHit(self, pc):
		
		setIndex = self.getSetIndex(pc)
		tag = self.getTag(pc)
		blo = self.getBlockOffset(pc)
		# print "SI: ", setIndex
		# print "TG: ", tag

		for block in range(0, 2):
			if (tag == self.ch[setIndex][block][2]) and (self.ch[setIndex][block][0] == 1):
				return [setIndex, block, blo]
		return [None, None, None]

	def getData(self, pc):
		# Discover if pc is in cache.
		hit = self.isHit(pc)
		if hit[0] != None:
			return self.ch[hit[0]][hit[1]][hit[2]+3]
		else:
			return None

	def write(self, mAddr, data):
		# If dirty bit off, simply write over the existing cache data.
		hit = self.isHit(mAddr)
		if hit[0] != None:
			pass

		# If dirty bit on, return the data that WAS held there to memory.