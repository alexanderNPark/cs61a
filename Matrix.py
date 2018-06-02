class Matrix(object):

    class Row(list):
        def __init__(self,lst):
            super(list,self).__init__()
            for i in lst:
                self.append(i)

        def multiplyBy(self, constant):
            return [e*constant for e in self]

        def addRow(self,another_row):
            if(type(another_row) is Matrix.Row):
                for i in range(self.column_size):
                    self[i]+=another_row[i]

        @property
        def column_size(self):
            return len(self)

        def __repr__(self):
            string=""
            for element in self:
                string+=str(element)+" "
            return string

    class VectorSizeNotCongruent(Exception):
        pass

    def __init__(self,two_dimension):
        self.row_size = len(two_dimension)
        self.content = [Matrix.Row(row) for row in two_dimension]
        self.is_augmented = len(self.content)<len(self.content[0])
        self.is_square = len(self.content)==len(self.content[0])

    def solve(self):
        if(self.is_square):
            return None
        for pivot_column in range(len(self.content[0])-1):
            if(self.is_free_column(pivot_column)):
                continue
            for row in range(len(self.content)):




    def first_non_zero_pivot_swap(self,column_num):

        for i in range(len(self.content)-column_num):



        return True


    def



    def __repr__(self):
        string = ""
        for i in self.content:
            string +=repr(i)+"\n"
        return string


def start():
    str=""
    matrix = []
    while(True):
        line = input("Row:")
        if(line=='end'):
            break
        numbers = line.split()
        matrix.append(list(map(int,numbers)))
    m = Matrix(matrix)
    print(m)
    print(m.is_augmented)

start()