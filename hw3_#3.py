o = open("output.txt", "w")
try:
    f = open("input.txt")
except FileNotFoundError:
    out.write("файла не существует")
else:
    a = f.readlines()
    d = input()
    w = dict()
    for i in a:
        p = i.replace(" ", "")
        x = p.split(":")
        s = x[1].split(",")
        for j in s:
            if j in w:
                w[j].append(x[0])
            else:
                w[j] = [x[0]]
    for i in w[d]:
        o.write(i +"\n")
    f.close()
o.close()
