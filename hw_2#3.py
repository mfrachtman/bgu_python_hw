f = open("input1.txt")
m = open("input2.txt")
a = f.readlines()
d = m.readlines()
s = a + d
s.sort()
t = open("output.txt", "w")
for i in s:
	t.write(i.strip() + "\n")
t.close()
