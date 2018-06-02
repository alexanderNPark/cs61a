from operator import add, mul

def square(x):
    return x * x

def triple(x):
    return 3 * x

def identity(x):
    return x

def increment(x):
    return x + 1

def summation(n, term):
    """Return the summation of the first n terms in a sequence.

    n    -- a positive integer
    term -- a function that takes one argument

    >>> summation(3, identity) # 1 + 2 + 3
    6
    >>> summation(5, identity) # 1 + 2 + 3 + 4 + 5
    15
    >>> summation(3, square)   # 1^2 + 2^2 + 3^2
    14
    >>> summation(5, square)   # 1^2 + 2^2 + 3^2 + 4^2 + 5^2
    55
    """
    "*** YOUR CODE HERE ***"
    sum,i=0,1
    while i <=n:
        sum+=term(i)
        i+=1
    return sum

def product(n, term):
    """Return the product of the first n terms in a sequence.

    n    -- a positive integer
    term -- a function that takes one argument

    >>> product(3, identity) # 1 * 2 * 3
    6
    >>> product(5, identity) # 1 * 2 * 3 * 4 * 5
    120
    >>> product(3, square)   # 1^2 * 2^2 * 3^2
    36
    >>> product(5, square)   # 1^2 * 2^2 * 3^2 * 4^2 * 5^2
    14400
    """
    "*** YOUR CODE HERE ***"

    sum = 1
    for i in range(1,n+1):
        sum*=term(i)
    return sum


# The identity function, defined using a lambda expression!
identity = lambda k: k

def make_adder(n):
    """Return a function that takes an argument K and returns N + K.

    >>> add_three = make_adder(3)
    >>> add_three(1) + add_three(2)
    9
    >>> make_adder(1)(2)
    3
    """
    "*** YOUR CODE HERE ***"
    return lambda x:x+n

def accumulate(combiner, base, n, term):
    """Return the result of combining the first n terms in a sequence and base.
    The terms to be combined are term(1), term(2), ..., term(n).  combiner is a
    two-argument commutative function.

    >>> accumulate(add, 0, 5, identity)  # 0 + 1 + 2 + 3 + 4 + 5
    15
    >>> accumulate(add, 11, 5, identity) # 11 + 1 + 2 + 3 + 4 + 5
    26
    >>> accumulate(add, 11, 0, identity) # 11
    11
    >>> accumulate(add, 11, 3, square)   # 11 + 1^2 + 2^2 + 3^2
    25
    >>> accumulate(mul, 2, 3, square)   # 2 * 1^2 * 2^2 * 3^2
    72
    """
    "*** YOUR CODE HERE ***"
    i = 1
    sum = base
    while i <= n:
        sum = combiner(sum,term(i))
        i+=1
    return sum

def summation_using_accumulate(n, term):
    """Returns the sum of term(1) + ... + term(n). The implementation
    uses accumulate.

    >>> summation_using_accumulate(5, square)
    55
    >>> summation_using_accumulate(5, triple)
    45
    """
    "*** YOUR CODE HERE ***"
    return accumulate(add,0,n,term)

def product_using_accumulate(n, term):
    """An implementation of product using accumulate.

    >>> product_using_accumulate(4, square)
    576
    >>> product_using_accumulate(6, triple)
    524880
    """
    "*** YOUR CODE HERE ***"
    return accumulate(mul,1,n,term)

def filtered_accumulate(combiner, base, pred, n, term):
    """Return the result of combining the terms in a sequence of N terms
    that satisfy the predicate PRED.  COMBINER is a two-argument function.
    If v1, v2, ..., vk are the values in TERM(1), TERM(2), ..., TERM(N)
    that satisfy PRED, then the result is
         BASE COMBINER v1 COMBINER v2 ... COMBINER vk
    (treating COMBINER as if it were a binary operator, like +). The
    implementation uses accumulate.

    >>> filtered_accumulate(add, 0, lambda x: True, 5, identity)  # 0 + 1 + 2 + 3 + 4 + 5
    15
    >>> filtered_accumulate(add, 11, lambda x: False, 5, identity) # 11
    11
    >>> filtered_accumulate(add, 0, odd, 5, identity)   # 0 + 1 + 3 + 5
    9
    >>> filtered_accumulate(mul, 1, greater_than_5, 5, square)  # 1 * 9 * 16 * 25
    3600

    """
    def combine_if(x, y):
        "*** YOUR CODE HERE ***"
        if pred(y) is True:
            return combiner(x,y)
        else: return x
    return accumulate(combine_if, base, n, term)

def odd(x):
    return x % 2 == 1

def greater_than_5(x):
    return x > 5

def repeated(f, n):
    """Return the function that computes the nth application of f.

    >>> add_three = repeated(increment, 3)
    >>> add_three(5)
    8
    >>> repeated(triple, 5)(1) # 3 * 3 * 3 * 3 * 3 * 1
    243
    >>> repeated(square, 2)(5) # square(square(5))
    625
    >>> repeated(square, 4)(5) # square(square(square(square(5))))
    152587890625
    >>> repeated(square, 0)(5)
    5
    """
    "*** YOUR CODE HERE ***"
    def rpeat(value):
        nonlocal n
        if n<=0:
            return value
        n-=1
        return rpeat(f(value))
    return rpeat

def compose1(f, g):
    """Return a function h, such that h(x) = f(g(x))."""
    def h(x):
        return f(g(x))
    return h

def repeated2(f,n):
    """Return the function that computes the nth application of f.

        >>> add_three = repeated2(increment, 3)
        >>> add_three(5)
        8
        >>> repeated2(triple, 5)(1) # 3 * 3 * 3 * 3 * 3 * 1
        243
        >>> repeated2(square, 2)(5) # square(square(5))
        625
        >>> repeated2(square, 4)(5) # square(square(square(square(5))))
        152587890625
        >>> repeated2(square, 0)(5)
        5
        """
    def summatedFunction(val):
        return accumulate(lambda x,y: compose1(f,identity)(x),val,n,lambda x:0)
    return summatedFunction

def repeated3(f, n):
    """Return the function that computes the nth application of f.

            >>> add_three = repeated3(increment, 3)
            >>> add_three(5)
            8
            >>> repeated3(triple, 5)(1) # 3 * 3 * 3 * 3 * 3 * 1
            243
            >>> repeated3(square, 2)(5) # square(square(5))
            625
            >>> repeated3(square, 4)(5) # square(square(square(square(5))))
            152587890625
            >>> repeated3(square, 0)(5)
            5
            """
    return accumulate(compose1, lambda x: x, n, lambda k: f)

