##################################
# The MEM unit handles LDUR and STUR operations.
#LDUR
#	For LDUR, it takes one cycle to finish if it hits in the cache.
#	If it misses in the cache, then the operation cannot be performed and must be retried in the next cycle.
#	In this case, the operation remains in the pre-mem buffer.
#	When a cache hit occurs, the operation finishes and the instruction index (which gives you the destination reg for the writeback unit) and data will be written to the post-MEM buffer.

#STUR
#	A STUR takes one cycle to finish if there is room in the cache.
#	If it cannot write in the cache, then the operation cannot be performed and must be retried in the next cycle.
#	In this case, the operation remains in the pre-mem buffer.
#	When a cache write occurs, the STUR instruction  just finshes.
#	The STUR instruction never goes into the post-MEM buffer.
#	It just disappears.
#	Everyone gets updated in the same cycle that the write happens.
#	If the required set is full then you must figure out what to kick out on one cycle and write everything the next cycle.
#	This may cause a stall since you are checking to see that all instructions in flight that might access the memory location have to wait.
#	A RAW hazard.
##################################

class MemoryUnit(object):
    def __init__(self, cache):
        self.cache = cache
		self.content = 0
	def checkCache(self):
		pass
	def getContent(self):
		return self.content
	def setContent(self, content):
		self.content = content