class IR_List(object):
    class EmptyList(object):
        def __repr__(self):
            return "()"
    e = EmptyList()

    def __init__(self,first,rest=e):
        self.first = first
        if(type(self.first)==IR_List):
            self.is_deep_list = True
        self.rest=rest #must be another IR_List

    def add(self,element):
        if(self.rest==self.e):
            self.rest=IR_List(element)
            return
        self.rest.add(element)


    def __getitem__(self, item):
        if(self==self.e):
            return self.e
        elif(item==0):
            return self.first
        else:
            return self.rest[item-1]

    def extend(self,newIR_List):
        if(self.rest==self.e):
            self.rest = newIR_List
        else:
            self.rest.extend(newIR_List)

    def __repr__(self):
        if(self==self.e):
           return self.e.__repr__()
        else:
           return "IR_LIST("+(type(self.first)==IR_List and self.first.__repr__() or str(self.first)) +", "+ self.rest.__repr__()+")"

    def __len__(self):
        if(self.rest==self.e):
            return 1
        return 1+len(self.rest)

    def insert(self,index,element):
        if(index<0):
            return
        if (self.rest == self.e):
            self.rest = IR_List(element)
        elif(index==0):
            self.first,temp = element,self.first
            self.rest = IR_List(temp,self.rest)
        else:
            self.rest.insert(index-1,element)

    @staticmethod
    def reverse(irlist):
        if(irlist.rest == IR_List.e):
            return IR_List(irlist.first)
        if(type(irlist.first)==IR_List):
            temp = IR_List.reverse(irlist.first)
            augmented = IR_List.reverse(irlist.rest)
            augmented.add(temp)
            return augmented
        else:
            augmented = IR_List.reverse(irlist.rest)
            augmented.add(irlist.first)
            return augmented

    def load(self,list_or_tuple):
        if(len(list_or_tuple)==0):
            return
        self.rest = IR_List(list_or_tuple[0])
        self.rest.load(list_or_tuple[1:])

    @staticmethod
    def pop(irlist,index):
        prev,current= None,irlist
        while(index>0 and current!=current.e):
            prev=current
            current = current.rest
            index-=1
        if(index==0 and current!=current.e):
            if(prev==None):
                return current.rest
            else:
                prev.rest = current.rest
                return irlist
        else:
            return None

    def toList(self):
        list=[self.first]
        if(self.rest==self.e):
            return list
        list.extend(self.rest.toList())
        return list



    def count(self,element):
        count =0
        if (type(self.first) == IR_List):
            count += self.first.count(element)
        else:
            if (self.first == element):
                count += 1
        if(self.rest!=self.e):
            count += self.rest.count(element)
        return count

    def __add__(self, other):
        if(self.rest==self.e):
            if(type(other)==IR_List):
                return IR_List(self.first,other)
            else:
                return IR_List(self.first,IR_List(other))
        return IR_List(self.first,self.rest+other)

    def filterF(self,predicateFunction):
        if(type(self.first)==IR_List):
            return IR_List(self.first.filterF(predicateFunction), self.rest.filterF(predicateFunction))
        elif(predicateFunction(self.first)):
            if (self.rest != self.e):
                return IR_List(self.first, self.rest.filterF(predicateFunction))
            else:
                return IR_List(self.first)
        elif(self.rest!=self.e):
            return self.rest.filterF(predicateFunction)
        else:
            return self.e

    def map(self,function):
        if(type(self.first)==IR_List):
            return IR_List(self.first.map(function), self.rest.map(function))
        elif(self.rest==self.e):
            return IR_List(function(self.first))
        else:
            return IR_List(function(self.first),self.rest.map(function))








first = IR_List(4)
first.add(5)
first.add(5)
print(first)
second = IR_List(3)
second.add(2)
second.add(1)
combine = first+second
combine.insert(10,9)
combine.insert(3,10)
newCombine = (IR_List(combine+0)+5)
print(newCombine)
print(newCombine.count(5))
print(newCombine.map(lambda x:x%2 ))

reverseTest = IR_List(0)
reverseTest.load([1,2,3,4,5,6,7,8,9])
print(IR_List.pop(IR_List.reverse(reverseTest),4).toList())


#print(first)

