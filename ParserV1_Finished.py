from operator import add,sub,mul,truediv,pow,mod
def E(const,exp):
    return const*pow(10,exp)
def activate(function,*args):
    centralVal = args[0]
    for i in range(1,len(args)):
        centralVal = function(centralVal,args[i])
    return centralVal



class ExpressionParser_Basic(object):
    """
    Scheme interpeter ideally in form of post fix operation not prefix
    """
    def assign(self,name,value):
        self.name_bindings[name]=value

    def getNameBinding(self,name):
        a = self.name_bindings[name]
        return a

    @staticmethod
    def isOperator(character):
        if (character in ExpressionParser_Basic.functionTable.keys()):
            return True
        else:
            return False

    @staticmethod
    def isPairFunction(char):
         if (char in ExpressionParser_Basic.two_arg.keys()):
             return True
         else:
             return False

    @staticmethod
    def isNumber(char):
        if(char in "1234567890"):
            return True
        else:return False

    is_op = isOperator
    functionTable = {'+':add, '-':sub, '*':mul,'x':mul,'/':truediv,'^':pow, "E":E}
    two_arg = {'^':functionTable['^'], 'E':functionTable['E']}
    name_bindings = {}

    def bind(self,variable_name,value):
        self.name_bindings[variable_name]=value

    def evaulate_post(self,expression_post_infix):
        self.expression = expression_post_infix
        valueStack=[]
        tempVariableTable={}
        variableName=""
        bindingOccured=False
        while(len(self.expression)!=0):
            char = self.expression[0]
            if(self.is_op(char)):
                if(len(valueStack)==0):
                    return "NO PREFIX"
                else:
                    result = activate(self.functionTable[char],*valueStack)
                    valueStack.clear()
                    valueStack.append(result)
            elif(char=='('):
                expParenthesis = self.evaulate_post(self.expression[1:])
                valueStack.append(expParenthesis)
                if (len(variableName) > 0):
                    bindingOccured = True
            elif(char==')'):
                break
            elif(self.isNumber(char)):
                valueStack.append(int(char))
                if (len(variableName) > 0):
                    bindingOccured = True
            elif(char=='='):
                bindingOccured=True
            else:
                variableName = variableName + char

            if(bindingOccured):
                a = valueStack.pop()
                tempVariableTable[variableName] = a  # every recursive depth we need to know what variables were created
                self.assign(variableName, a)
                variableName = ""

            self.expression = self.expression[1:]
            bindingOccured=False

        if(len(valueStack)==1):
            return valueStack.pop()
        elif(len(variableName)>0):
            return self.name_bindings[variableName]
        elif(len(tempVariableTable)>0):
            return tempVariableTable[list(tempVariableTable.keys())[0]]
        else:
            return 0

def interpret():
    e = ExpressionParser_Basic()
    while(True):
        str = input(">>>")
        if(str=="exit"):break
        print(e.evaulate_post(str.replace(" ","")))






def numberOP(content):
    try:
        if('.' in content):
            return float(content)
        else:
            return int(content)
    except Exception as e:
        return None

class ExpressionTree(object):
    class Tree(object):
        functionTable = {'+': add, '-': sub, '*': mul, 'x': mul, '/': truediv, '^': pow,'%':mod}
        operatorPrecedence = {'+':1, '-':2, '*':3,"/":4,'^':5,'%':4}
        def __init__(self,data,left=None,right=None):
            self.left = left
            self.right = right
            self.data=data
            self.parenthesized=False

        def isFull(self):
            return self.left!=None and self.right!=None

        def isLeaf(self):
            return self.left==None and self.right==None

        def empty(self):
            return self.data==None
        def clear(self):
            if(self.isLeaf()):
                self.data=None
            else:
                self.left.clear()
                self.right.clear()

        def __repr__(self):
            str = ""+self.left.__repr__()+""+self.data+""+self.right.__repr__()
            if(self.parenthesized):
                return "("+str+")"
            else:
                return str
        def evaluate(self):

            f = ExpressionTree.Tree.functionTable[self.data]
            param1 = (type(self.left)==ExpressionTree.Tree)and self.left.evaluate() or self.left
            param2 = (type(self.right)==ExpressionTree.Tree)and self.right.evaluate() or self.right
            return f(param1,param2)

    def isOperator(self,char):
        return char in list(ExpressionTree.Tree.functionTable.keys())

    def precedenceCompare(self,char1,char2):
        return char2!="" and (ExpressionTree.Tree.operatorPrecedence[char1]-ExpressionTree.Tree.operatorPrecedence[char2])or -1



    def parse(self,expression):
        numberTemp=""
        self.expression = expression
        head = ExpressionTree.Tree(None)
        tempExp=head
        prevOperator=""
        while(len(self.expression)!=0):
            char = self.expression[0]
            if(char == '('):
                newHead = self.parse(self.expression[1:])
                newHead.parenthesized = True
                if(head.empty()):
                    head = newHead
                    newHead=None
            elif(self.isOperator(char)):
                operand = numberOP(numberTemp)
                numberTemp=""
                if(operand==None):
                    operand = newHead
                    newHead = None
                if(head.empty()):
                    head.data = char
                    head.left=operand

                elif(not head.empty()):

                    if(self.precedenceCompare(char,prevOperator)>=0):
                        tempExp.right = ExpressionTree.Tree(char,operand,None)
                        tempExp=tempExp.right
                    else:
                        tempExp.right = operand
                        newHead = ExpressionTree.Tree(char,head,None)
                        tempExp=head=newHead

                prevOperator=char

            elif(char==')' or char==';'):
                break
            else:
                numberTemp +=char
            self.expression = self.expression[1:]
        a= numberOP(numberTemp)
        tempExp.right = (a==None and newHead!=None) and  newHead or a
        return head



def testExpressionTree():
    a = ExpressionTree()
    while(True):
        d= str(input(">>>"))
        if(d=='exit'):break
        print(a.parse(d).evaluate())



testExpressionTree()






