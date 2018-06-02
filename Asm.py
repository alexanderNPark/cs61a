class BinaryList(list):

    def __rshift__(self,other):
        if(other%4==0):
            return self.__getitem__(other//4)
        if(other%2==0):
            offset = other//4
            leftover = self.__getitem__(offset+1)
            remaining_bytes = other%4
            leftover=remaining_bytes*8