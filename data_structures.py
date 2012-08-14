

class ArrayDict(object):
	def __init__(self):
		super(ArrayDict, self).__init__()
		self.__data = {}

	def put(self, key, value):
		values = self.__data.get(key, [])
		values.append(value)
		self.__data[key] = values

	def get(self, key):
		return self.__data.get(key, [])
