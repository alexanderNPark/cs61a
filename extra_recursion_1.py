"""

Extra Recursion Practice 1
Trees and Linked Lists

@author: Alvin Wan
@site: alvinwan.com
"""

##############
# QUESTION 1 #
##############

def set_tree_value(t, v):
    t[0] = v

# solution provided by CS61A student Kazu Kogachi
def max_by_level(t):
    """ Modify the tree, so that each value is replaced with the maximum
    value on that level of the tree. Use only your standard tree abstraction
    functions and set_tree_value, which is defined only for this problem.

    >>> t = tree(4, [tree(5), tree(7)])
    >>> max_by_level(t)
    >>> root(branches(t)[0])
    7
    """
    ### YOUR CODE HERE ###
    if (is_leaf(t)):
        return
    max_val = 0
    for child in branches(t):
        max_val = max(max_val, root(child))
        max_by_level(child)

    for child in branches(t):
        set_tree_value(child,max_val)




##############
# QUESTION 2 #
##############

def switch_every_third(link):
    """ MODIFY the linked list, where every third element is swapped with the
    first, considering each subset of three links where the first element of
    one subset is the last of the previous subset.

    >>> l = Link(1, Link(2, Link(3)))
    >>> switch_every_third(l)
    >>> print_list(l)
    3 2 1

    >>> l = Link(1, Link(2, Link(3, Link(4, Link(5)))))
    >>> switch_every_third(l)
    >>> print_list(l)
    3 2 5 4 1
    """
    ### YOUR CODE HERE ###
    if(link==Link.empty):
        return
    switch_every_third()

# solution provided by CS61A student Dibya Jyoti Ghosh
def new_switch_every_third(t):
    """ Return a NEW linked list, where every third element is swapped with the
    first, considering each subset of three links where the first element of
    one subset is the last of the previous subset.

    >>> a = Link(1,Link(2,Link(3)))
    >>> print_list(switch_every_third(a))
    3 2 1
    >>> a = Link(1,Link(2,Link(3,(Link(4,Link(5))))))
    >>> print_list(switch_every_third(a))
    3 2 5 4 1
    """
    ### YOUR CODE HERE ###


##############
# QUESTION 3 #
##############

def set_recursive(link):
  """ Return a linked list, where every third element is swapped with the
  first in EACH set of three.

  >>> l = Link(1, Link(2, Link(3)))
  >>> print_list(set_recursive(l))
  3 2 1
  >>> l = Link(1, Link(2, Link(3, Link(4, Link(5, Link(6))))))
  >>> print_list(set_recursive(l))
  3 2 1 6 5 4
  """
  ### YOUR CODE HERE ###


#####################
# TREE ABSTRACTIONS #
#####################

tree = lambda root, branches=[]: [root, branches]
root = lambda t: t[0]
branches = lambda t: t[1]
is_leaf = lambda t: not branches(t)

#############
# UTILITIES #
#############

class Link:
  """ Link object """
  empty = None

  def __init__(self, first, rest=None):
    self.first = first
    self.rest = rest

def print_list(lst):
    """Printing utility for linked lists

    >>> print_list(Link(5))
    5
    >>> print_list(Link(3, Link(4, Link(5))))
    3 4 5
    """
    def helper(link):
        if link is Link.empty:
            return []
        return [link.first] + helper(link.rest)
    print(*helper(lst))
