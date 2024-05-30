def sum(a):
	s = 0
	for i in a:
		s += int(i)
	return s
a = input()
while sum(a) > 9:
	a = str(sum(a))
print(sum(a))