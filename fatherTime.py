from time import sleep

class time(object):
	"""docstring for time"""

	epoch = 0

	def __init__(self, epochLength=0.1, endOfTime=5000):
		super(time, self).__init__()
		self.epochLength = epochLength
		self.endOfTime = endOfTime



	def epochElapsed(self):
		sleep(self.epochLength)
		self.epoch += 1
		return self.epoch
		