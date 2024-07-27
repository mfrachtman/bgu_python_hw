def f(n, m):
    if n == 0 or m == 0:
        return n+m
    if n > m:
        return f(n-m,m)
    else:
        return f(n, m-n)
n = int(input())
m = int(input())
print(f(n,m))
