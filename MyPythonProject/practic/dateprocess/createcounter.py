def createcounter():
    x=0
    def counter():
        nonlocal x
        x=x+1
        return x
    return counter
counterA = createcounter()
print(counterA(), counterA(), counterA(), counterA(), counterA())  
counterB = createcounter()
if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
    print('测试通过!')
else:
    print('测试失败!')

print(list(map(lambda x: x * x, (x for x in range(15)))))

def is_odd(n):
    return n % 2 == 1
print(list(filter(is_odd, range(1, 20))))
print(list(filter(lambda n:n%2==1, range(1, 20))))