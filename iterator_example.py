class Cards(object):
    def __init__(self):
        from random import randint
        self.content = [randint(0,1000) for i in range(10)]

    def __iter__(self):
        return self.Iterator(self)

    def gen(self):
        i=0
        while(i<len(self.content)):
            yield self.content[i]
            i+=1

    class Iterator(object):

        def __init__(self,holder):
            self.content_to_iter = holder
            self.i=0

        def __iter__(self):
            return self


        def __next__(self):

            if(self.i>=len(self.content_to_iter.content)):
                raise StopIteration()

            #print("inside iterator ", self.i)
            val = self.content_to_iter.content[self.i]
            self.i+=1
            return val





a,b,c = 5,6,7
a,b,c = b,c,a = c,a,b #a,b,c->6,7,5

print(a,b,c)
