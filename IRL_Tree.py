class IRL_Tree(object):

    def __init__(self, value, leafs):
        self.value = value
        self.branches = leafs

    def is_leaf(self):
        if(self.branches is None):
            return True
        return False

    def __repr__(self):
        if(self.is_leaf()):
            return str(self.value)
        return "< "+str(self.value)+" < "+",".join([repr(e) for e in
                                                 self.branches])+" > "




    def size(self):
        if(self.is_leaf()):
            return 1
        else:
            sum = 1
            for element in self.branches:
                sum+=element.size()
            return sum



tree = IRL_Tree(5,[IRL_Tree(3,[IRL_Tree(1, None)]), IRL_Tree(2,[IRL_Tree(9,
                                                                         None
                                                                         )])])
print(repr(tree))


