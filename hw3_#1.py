o = open("filtered_cities.txt", "w")
try:
    f = open("cities.txt")
except FileNotFoundError:
    out.write("файла не существует")
else:
    s = f.readlines()
    s.sort()
    a = int(input())
    for i in s:
        r = i.split(":")
        if int(r[1]) > a:
            out.write(r[0] + "\n")
    f.close()
o.close()