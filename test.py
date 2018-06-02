def coin_denom(value, denoms):
    if(denoms==[] or value<0):
        return None
    if(value==0):
        return [[]]
    else:
        result = []
        val = coin_denom(value-denoms[0],denoms)
        next = coin_denom(value,denoms[1:])

        if(val is not None):
            for e in val:
                result.append([denoms[0]]+e)
        if(next is not None):
            result.extend(next)
        return result





#print(coin_denom(10, [25,10,5,1]))
a = [i for i in range(10)]
print(iter(a))
b = iter(a)
print(b is iter(a))
print(b == iter(a))
c = b
next(c)
def b(iterab):
    print("inside generator")
    a = iter(iterab)
    while(True):
        print(a,"is iterator ")
        yield next(a)
d = b(c)

class A(object):

    def __init__(self):
        self.x = 10
        self.g = A.func2

    def func1(self):
        print("Original func1",self.z)
    def func2(self,item):
        print(self.z)
        print(item)

class B:
    def __init__(self):
        self.z = 5
        A.__init__(self)


d = B()
B.s=A.func2
d.s(2)
















