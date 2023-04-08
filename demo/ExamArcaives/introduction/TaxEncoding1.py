c = 0


def str_sum(*a):
	b = a[0]
	for _ in a[1:]:
		b += _
	return b


a = lambda x: tuple(map((lambda f: bin(ord(f))), x))


def z(*a):
	global c
	c2 = max(map(len, a))
	c = c2
	e = []
	for _ in a:
		d = c - len(_)
		d = '0' * d
		d += _[2:]
		e.append(d)
	return tuple(e)


def haha(x, hahaha):
	seq = x
	length = hahaha
	return [seq[i:i + length] for i in range(0, len(seq), length)]


def y(x):
	return str_sum(*z(*a(x)))


def hoho(x):
	global c
	return str_sum(*tuple(map((lambda x: chr(int(x, 2))), haha(x, c - 2))))
