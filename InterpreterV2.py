class NotEnoughElements(Exception):
    def __repr__(self):
        return "Needs at least one element for:" + self.operator

    def __init__(self, operator):
        self.operator = operator




class InvalidExpression(Exception):
    def __init__(self,operator='()'):
        super().__init__("Parenthesis Unbalanced")
        self.operator = operator


start_char = '('
end_char = ')'
name_bindings = {'pi':'3.14','isp':'#t'} #predefined constants
conversion = {'False':'#f','True':'#t'}# boolean conversion constants for results

def add(operands):
    length = len(operands)
    assert not (length == 0), "Not enough elements"
    if (length == 1): return operands[0]
    return operands[0] + add(operands[1:])


def subtract(operands):
    length = len(operands)
    assert not (length == 0), "Not enough elements"
    if (length == 1):
        return -operands[0]
    else:
        difference = operands[0]
        for i in range(1, len(operands)):
            difference -= operands[i]
        return difference


def multiply(operands):
    length = len(operands)
    assert not (length == 0), "Not enough elements"
    if (length == 1):
        return operands[0]
    return operands[0] * multiply(operands[1:])


def divide(operands):
    length = len(operands)
    assert not (length == 0), "Not enough elements"
    if (length == 1):
        return operands[0]
    return float(operands[0] / divide(operands[1:]))


def define(operands):
    assert not (operands[0] in list(name_bindings.keys())), str(operands[0]) + " already exists"
    name_bindings[operands[0]] = operands[1]
    return operands[1]


def set_funct(operands):
    assert (operands[0] in list(name_bindings.keys())), str(operands[0])+" does not exist"

    name_bindings[operands[0]] = operands[1]
    return operands[1]

def convert(result):
    try:
        return conversion[result]
    except:
        return result


def and_function(operands):
    assert not (len(operands) < 2), "Needs two or more numbers"
    result = operands[0]

    if(not result):
        return convert(str(result))

    for i in range(len(operands)):
        result = result and operands[i]
    return convert(str(result))


def or_function(operands):
    assert not (len(operands) < 2), "Needs two or more numbers"

    result = operands[0]
    if(result):
        return convert(str(result))
    for i in range(len(operands)):
        result = result or operands[i]
    return convert(str(result))


def not_function(operands):
    assert not (len(operands) == 0 or len(operands) > 1), "Cannot 'Not' two expression primitives"
    return convert(not operands[0])






class Expression(object):
    expression_operator_table = {'+': add, '-': subtract, '*': multiply,
                                 '/': divide,'|': or_function, '&': and_function, '!': not_function,
                                 '=':0,'>=':0,'>':0,"<":0,'<=':0}  # only allow permitted operators for regular expressions
    boolean_operator_only = {'|': or_function, '&': and_function, '!': not_function,'=':0}
    constant_values = { '#t': True, '#f': False}

    def __init__(self, operator):
        self.operands = []
        self.operator = operator
        self.is_literal = False

    def check_list_instance(self):
        if (not self.operator in list(self.expression_operator_table.keys())):
            self.is_list = True

    def addOperand(self, element):
        self.operands.append(element)

    def is_primitive(self):
        return self.operator is None

    def setEnv(self,env=name_bindings):
        self.env = env

    def __repr__(self):
        result = start_char + repr(self.operator == None and "" or self.operator)
        for i in range(len(self.operands)):
            result += ("," + repr(self.operands[i]))
        return result + end_char

    def check_validity(self):
        values = set(self.operands)

    def evaluate(self):
        temp_operands = []
        i = 0
        while (i < len(self.operands)):
            operand = self.operands[i]
            if (isinstance(operand,Expression)):
                temp_operands.append(operand.evaluate())
            else:
                if (operand in list(self.constant_values.keys())):
                    temp_operands.append(operand)
                elif (operand in list(name_bindings.keys())):  # check for variable binding
                    temp_operands.append(name_bindings[operand])
                else:
                    temp_operands.append(operand)
            i += 1

        self.give_type(temp_operands)

        return self.eval_directly(temp_operands)

    def eval_directly(self, operands):
        assert (self.operator in list(self.expression_operator_table.keys())),"No such Operand Exists"
        if(self.operator not in list(self.boolean_operator_only.keys())):
            assert self.is_boolean_exp==False, "Cannot Perform Integer Operations on Boolean Values"
        return str(self.expression_operator_table[self.operator](operands))

    def give_type(self, operands):
        self.is_boolean_exp = False
        for i in range(len(operands)):
            try:
                if ('.' in operands[i]):
                    operands[i] = float(operands[i])

                elif('#' in operands[i]):
                    operands[i] = Expression.constant_values[operands[i]]
                    self.is_boolean_exp = True

                else:
                    operands[i] = int(operands[i])
            except:
                raise InvalidExpression()





class Literal(Expression):
    expression_operator_table = {'\'': 0}

    def __init__(self):
        super().__init__('\'')
        self.is_literal = True

    def evaluate(self):
        result = ""
        for element in self.operands:
            result +=str(element)+" "
        return result

"""
Anything in scheme which has the option of not having a space like (+4 5) needs to form parsing to tokenize with spaces
however, it is enforced that inside each expression of parenthesis that every textual operator must be divided by spaces in the first place
like (define x 5) vs (define x5) in which the latter will throw an error since there is no second operand
An instance in which you need to make sure an operator is not confused is (define definex 5) where with definex it will form two tokens 
because define will be replaced with ' define x' which should not happen therefore all name_bindings,constants, and definitions will not be replaced
with itself plus space delimiters but instead assumed to be attached to space rules within expression pararenthesis.
So therefore non-symbolic aka textual operators or names cannot be space delimited but processed as tokens and checked in expression building or 
upon expression creation constructor
"""

special_characters =  [list(Expression.expression_operator_table.keys()),
                      [start_char, end_char],
                      list(Literal.expression_operator_table.keys()),list(Expression.constant_values.keys())]

def is_special(element):
    for char_set in special_characters:
        if (element in char_set):
            return True
    return False

def tokenize(string_expression):
    newString = ""
    if (not string_expression.startswith('(')):
        string_expression = start_char + string_expression + end_char
    for e in string_expression:
        if (is_special(e)):
            newString += (" " + e + " ")
        else:
            newString += e
    return [e for e in list(newString.split(' ')) if (e != '')]

def is_valid(string_tokens):
    i = 0
    count = 0
    while (i < len(string_tokens) and count >= 0):
        token = string_tokens[i]
        if (token == start_char):
            count += 1
        elif (token == end_char):
            count -= 1
        i += 1
    return count == 0

def transform(string_tokens):
    expression = None
    while (len(string_tokens) > 0):
        e = string_tokens[0]
        if (e == end_char):
            string_tokens.pop(0)
            return expression
        elif (e == start_char):
            string_tokens.pop(0)
            expression = buildExpression(string_tokens)
            continue
    raise InvalidExpression()

def buildExpression(string_tokens):
    operator_token = string_tokens.pop(0)
    if (operator_token in Literal.expression_operator_table.keys()):
        e = Literal()
    else:
        e = Expression(operator_token)
    while (string_tokens[0] != end_char and len(string_tokens) > 0):

        if (string_tokens[0] == start_char and type(e)!=Literal):
            string_tokens.insert(0, transform(string_tokens))
        e.addOperand(string_tokens.pop(0))


    if (len(string_tokens) == 0):
        raise InvalidExpression()

    return e

def testFunction():
    while (True):
        a = input('>>>')
        tokens = tokenize(a)
        e = transform(tokens)
        print(e.evaluate())

testFunction()
