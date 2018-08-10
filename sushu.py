def _odd():
	n=1;
	while True:
		n+=2
		yield n

def fil(n):
	return lambda x:x%n>0

def sushu():
	yield 2;
	it=_odd();
	while True:
		n=next(it);
		yield n;
		it=filter(fil(n),it)

for n in sushu():
	if n<1000:
		print(n)
	else:
		break