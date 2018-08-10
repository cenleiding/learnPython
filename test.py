def createCounter():
	i=[0]
	def counter():
		i[0]=i[0]+1
		return i[0]
	return counter

counterA = createCounter()
print(counterA(), counterA(), counterA(), counterA(), counterA())

