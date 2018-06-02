def instantiate(cls):
    def getValue(name):
        if(name in instance_attributes):
             val = instance_attributes[name]
        else:
            val = class_attributes_dict['get'](name)
        if(callable(val)):
            return lambda *args:val(instance_methods_dicts,*args)
        else:
            return val

    def setValue(name,value):
       instance_attributes[name]=value

    def list_all_method_attributes():
        methods = class_attributes_dict['list_all_methods']()
        for key,value in instance_attributes.items():
            if(callable(value)):
                methods.append(key)
        return methods

    def list_all_variables():
        variables = class_attributes_dict['list_all_value_variables']()
        for key,value in instance_attributes.items():
            if(not callable(value)):
                variables.append(key)
        return variables

    class_attributes_dict = cls  # The class is a dictionary
    instance_attributes = {}
    instance_methods_dicts = {'set':setValue, 'get':getValue, 'list_all_methods':list_all_method_attributes , 'list_all_value_variables':list_all_variables}
    return instance_methods_dicts

def make_class(nameOfClass, superClass=None): #does not allow classmethods or static methods
    def getValue(name):
        if(name in class_attributes):
            return class_attributes[name]
        elif(superClass is not None):
            return superClass['get'](name)
    def setValue(name, value):
        class_attributes[name]=value

    def list_all_method_attributes():
        methods = []

        if(superClass is not None):methods = superClass['list_all_methods']()
        for key,value in class_attributes.items():
            if(callable(value)):
                methods.append(key)
        return methods

    def list_all_variables():
        variables = []
        if (superClass is not None):variables = superClass['list_all_value_variables']() # make sure that your list includes all of the superclasses

        for key,value in class_attributes.items():
            if(not callable(value)):
                variables.append(key)
        return variables

    def instantiateAndInitialize(*args):
        instance = instantiate(class_attributes_dicts)
        if (instance['get']('__init__')):
            instance['get']('__init__')(*args)
        return instance

    class_attributes_dicts= {'get':getValue, 'set':setValue, 'list_all_methods':list_all_method_attributes ,
                             'list_all_value_variables':list_all_variables, 'new':instantiateAndInitialize}
    class_attributes = {"__name__":nameOfClass}
    return class_attributes_dicts


def build_Person_Class():
    person = make_class("Person",None)
    def __init__(self,balance,age,date_of_birth):
        self['set']('balance',balance)
        self['set']('age',age)
        self['set']('date_of_birth', date_of_birth)
    def qualifyForDriving(self):
        return self['get']('age') >=21 and True or False
    person['set']('__init__',__init__)
    person['set']('qualifyForDriving', qualifyForDriving)
    return person

def testBindableMethod(self, a):
    self['set']('square', (lambda a: lambda this,x:a*x)(a))

"""
Person = build_Person_Class()
p = Person['new'](200,20,"Decemeber")
print(p['get']('qualifyForDriving')())
print(p['list_all_methods']())
p['set']('test_function', testBindableMethod)
p['get']('test_function')(10)
print(p['list_all_methods']())
print (p['get']('square')(5))


p['get']('test_function')(20)
print(p['get']('square')(5))
"""

"""
first = make_class('First')
first['set']('__name__',"First_Class")
firstInstance = instantiate(first)
print(firstInstance['get']("__name__"))
firstInstance['set']('balance', 100)
print(firstInstance['list_all_value_variables']())
firstInstance['set']('lambda1', lambda x:x*x)
print (firstInstance['get']('lambda1')(4))
"""

class Complex_Number_61A(object):

    def __init__(self, val1, val2, polarForm=False):
        if(polarForm):
            self.polar_form = (val1,val2)
            self.complexForm()

        else:
            self.complex_form = (val1,val2)
            self.polarForm()

    def __add__(self, other):
        if (type(other) == Complex_Number_61A):
            return Complex_Number_61A(other.complex_form[0]+self.complex_form[0], other.complex_form[1]+self.complex_form[1])
        if(type(other) == int):
            return Complex_Number_61A(other+self.complex_form[0], self.complex_form[1])
        else:
            return None


    def __str__(self):
        return str(self.complex_form[0])+"+"+str(self.complex_form[1])+"j"

    def __repr__(self):
        return self.__str__()

    def polarForm(self):
        pythagorean_function = lambda x,y: (x**2+y**2)**0.5
        from math import atan
        from functools import reduce
        self.polar_form = (reduce(pythagorean_function, self.complex_form), atan(self.complex_form[1]/self.complex_form[0]))


    def complexForm(self):
        from math import sin,cos
        buildReal = lambda : self.polar_form[0]*cos(self.polar_form[1])
        buildImaginary = lambda: self.polar_form[0]*sin(self.polar_form[1])

        self.complex_form = (buildReal(), buildImaginary())

    def __mul__(self, other):
        if(type(other) == int):
            other = Complex_Number_61A(other,0)
        if(type(other) == Complex_Number_61A):
            return Complex_Number_61A(self.polar_form[0]*other.polar_form[0], self.polar_form[1]+other.polar_form[1], True)
        else:
            return None

    @staticmethod
    def degrees_to_radian(degrees_angle):
        from math import pi
        return degrees_angle*pi/180

    def get_real(self): return self.complex_form[0]
    def get_imaginary(self):return self.complex_form[1]
    def get_angle(self):return self.polar_form[1]
    def get_magnitude(self): return self.polar_form[0]

from math import sqrt
compOne = Complex_Number_61A(10,5)
compTwo = Complex_Number_61A(10,Complex_Number_61A.degrees_to_radian(45), True)
compThree = Complex_Number_61A(12,6)
final = compOne+compTwo
print(compOne*6)


