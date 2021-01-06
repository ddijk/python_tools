def fibon(n):
    a = b = 1
    for i in range(n):
        yield a
        a, b = b, a + b

gen = fibon(6)

print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
