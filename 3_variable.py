x = 10
y = "Python is new for me"
z = 144 ** 0.5  == 12

print(x)
print(y)
print(z)

x = 10 * 10
print(x)

n = m = 30
print(n, m)

n, m, o = (1, 2, 3)
print(n, m, o)

o, n = n, o
print(n, m, o)

a = "Hello World"
b = a
b = b.lower()
print(a)
print(b)

# lists mutable object -> sehingga kalau variable asignee value diganti, reference nya pengaruh
f = [1, 2, 3]
g = f
g.append(4)
print(f)
print(g)