class IR_Tree(object):
    class Empty(object):
        def __repr__(self):
            return "()"

    e = Empty()

    def __init__(self, entry, right=e, left=e):

        self.data = entry
        self.right = right
        self.left = left

    def isLeaf(self):
        return self.left==self.e and self.right==self.e or False

    def add(self,element):
        if(self.data==None and self.isLeaf()):
            self.data = element
            return
        if(self.data<element):
            if(self.right==self.e):
                self.right = IR_Tree(element)
                return
            else:
                self.right.add(element)
                return
        elif(self.data>element):
            if(self.left==self.e):
                self.left = IR_Tree(element)
                return
            else:
                self.left.add(element)
                return
        else:
            return

    def __repr__(self):
        return str(self.data)+"->[LEFT:"+self.left.__repr__()+",RIGHT:"+self.right.__repr__()+"]"

    def toList(self):
        list = []
        if(self.left!=self.e):
            list.extend(self.left.toList())
        list.append(self.data)
        if(self.right!=self.e):
            list.extend(self.right.toList())
        return list

    def loadOrdered(self,list):
        if(len(list)==0):
            return
        else:
            self.add(list[0])
        self.loadOrdered(list[1:])

    def clear(self):
        self.left=None
        self.right=None
        self.data=None



"""
first = IR_Tree(5)
first.add(6)
first.add(4)
first.add(3)
print(first.toList())
first.loadOrdered([8,9,10,1,2])
print(first)
"""