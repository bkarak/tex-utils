

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

	def has_key(self, key):
		return (len(self.get(key)) == 0)

	def keys(self):
		return self.__data.iterkeys()

	def __str__(self):
		return self.__data.__str__()
