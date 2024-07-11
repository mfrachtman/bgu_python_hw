t = open("output.txt", "w")
try:
	f = open("input.txt")
exсept FileNotFoundError:
	t.write("файл не сущ-ет")
else:
	a = f.readlines()
	s = 0
	for i in a:
		r = i.strip().split(",")
		s += int(r[1])
	s = s / len(a)
	for i in a:
		r = i.split(",")
		if int(r[1]) > s:
			t.write(r[0] + "\n")
	f.close()
t.close()
