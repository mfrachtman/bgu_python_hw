o = open("output.txt", "w")
try:
    f = open("input.txt")
except FileNotFoundError:
    out.write("файла не существует")
else:
    a = f.readlines()
    w = {"[" : "]", "<" : ">", "(" : ")", "{" : "}"}
    st = []
    q = ["[", "]", "{", "}", "<", ">", "(", ")"]
    for i in a:
        st = []
        for j in i.strip():
            if j in q:
                if len(st) != 0 and st[-1] in w and w[st[-1]] == j:
                    st.pop()
                else:
                    st.append(j)
        if len(st) != 0:
            o.write("False" + "\n")
        else:
            o.write("True" + "\n")
f.close()
o.close()
    
