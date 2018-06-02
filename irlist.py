"""The irlist module contains functions implementing the immutable
recursive list (IRList) data abstraction for CS61A at UC Berkeley.

IRLists are immutable recursive lists (an alternative to tuples), which
implements a common data structure found in most other programming languages.

One might notice that none of the doctests for either ADT actually "show" an
IRList. This is because this ADT is meant to be treated as a black box: the
tests do not assume any specific implementation for IRLists.
"""


# Immutable Recursive Lists Abstraction


empty_irlist = () # The empty immutable recursive list.


def make_irlist(first, rest=empty_irlist):
    """Make a new immutable recursive list by prepending item first to the
    front of the immutable recursive list rest (the empty immutable recursive
    list by default).
    """
    return (first, rest)


def irlist_first(irlist):
    """Return the first item in the immutable recursive list irlist.
    
    >>> irlist_first(make_irlist(5))
    5
    >>> irlist_first(make_irlist(1, make_irlist(2)))
    1
    """
    return irlist[0]


def irlist_rest(irlist):
    """Return an immutable recursive list of all the items except the first
    item in immutable recursive list irlist.

    >>> irlist_str(irlist_rest(make_irlist(5)))
    '<>'
    >>> irlist_str(irlist_rest(make_irlist(1, make_irlist(2))))
    '<2>'
    """
    return irlist[1]


def could_be_irlist(x):
    """Returns True if x might be an irlist."""
    def is_valid_empty(l):
        return l is empty_irlist
    def is_valid_non_empty(l):
        is_non_empty = type(l) is tuple and len(l) == 2
        return is_non_empty and could_be_irlist(irlist_rest(l))
    return is_valid_empty(x) or is_valid_non_empty(x)


# Immutable Recursive Lists Utilities


def irlist_populate(*items):
    """Populate a new irlist with the given items.

    >>> test_irlist = make_irlist(1, make_irlist(2, make_irlist(3)))
    >>> irlist_str(test_irlist)
    '<1, 2, 3>'
    >>> irlist_str(irlist_populate(1))
    '<1>'
    >>> irlist_str(irlist_populate())
    '<>'
    """
    if len(items) == 0:
        return empty_irlist
    populated_rest = irlist_populate(*items[1:])
    return make_irlist(items[0], populated_rest)


def irlist_len(irlist):
    """Return the length of irlist.

    >>> irlist_len(empty_irlist)
    0
    >>> irlist_len(irlist_populate(1, 2, 3, 4, 5))
    5
    """
    if irlist == empty_irlist:
        return 0
    return 1 + irlist_len(irlist_rest(irlist))


def irlist_select(irlist, index):
    """Return an item at the position index in irlist.
    
    >>> test_irlist = irlist_populate(1, 2, 3)
    >>> irlist_select(test_irlist, 0)
    1
    >>> irlist_select(test_irlist, 2)
    3
    """
    if index == 0:
        return irlist_first(irlist)
    return irlist_select(irlist_rest(irlist), index - 1)


def irlist_remove(irlist, index):
    """Remove the item at position index in irlist.

    >>> test_irlist = irlist_populate(1, 2, 3)
    >>> irlist_str(irlist_remove(test_irlist, 0))
    '<2, 3>'
    >>> irlist_str(irlist_remove(test_irlist, 2))
    '<1, 2>'
    """
    if index == 0:
        return irlist_rest(irlist)
    updated_rest = irlist_remove(irlist_rest(irlist), index - 1)
    return make_irlist(irlist_first(irlist), updated_rest)


def irlist_insert(irlist, index, item):
    """Replace the value at position index in irlist with item.

    >>> test_irlist = irlist_populate(1, 2)
    >>> irlist_str(irlist_insert(test_irlist, 0, 5))
    '<5, 2>'
    >>> irlist_str(irlist_insert(test_irlist, 1, 22))
    '<1, 22>'
    """
    if index == 0:
        return make_irlist(item, irlist_rest(irlist))
    updated_rest = irlist_insert(irlist_rest(irlist), index - 1, item)
    return make_irlist(irlist_first(irlist), updated_rest)


def irlist_append(irlist1, irlist2):
    """Append irlist2 to the end of irlist1.

    >>> test_irlist = irlist_populate(1, 2)
    >>> irlist_str(irlist_append(test_irlist, empty_irlist))
    '<1, 2>'
    >>> irlist_str(irlist_append(empty_irlist, test_irlist))
    '<1, 2>'
    >>> test_irlist2 = irlist_populate(1, 2, 3)
    >>> irlist_str(irlist_append(test_irlist, test_irlist2))
    '<1, 2, 1, 2, 3>'
    """
    if irlist1 == empty_irlist:
        return irlist2
    updated_rest = irlist_append(irlist_rest(irlist1), irlist2)
    return make_irlist(irlist_first(irlist1), updated_rest)


def irlist_filter(pred, irlist):
    """Filter through the irlist, removing any items that do not
    satisfy the predicate.

    >>> test_irlist = irlist_populate(1, 2, 3, 4, 5)
    >>> irlist_str(irlist_filter(lambda x: x % 2 == 0, test_irlist))
    '<2, 4>'
    >>> irlist_str(irlist_filter(lambda x: x % 2 == 1, test_irlist))
    '<1, 3, 5>'
    """
    filtered_irlist = empty_irlist
    while irlist is not empty_irlist:
        first = irlist_first(irlist)
        if pred(first):
            filtered_irlist = irlist_append(filtered_irlist, make_irlist(first))
        irlist = irlist_rest(irlist)
    return filtered_irlist


def irlist_map(func, irlist):
    """Applies a function to every item in the irlist, returning 
    the resulting irlist.

    >>> test_irlist = irlist_populate(1, 2, 3, 4, 5)
    >>> irlist_str(irlist_map(lambda x: x * x, test_irlist))
    '<1, 4, 9, 16, 25>'
    """
    mapped_irlist = empty_irlist
    while irlist is not empty_irlist:
        first = irlist_first(irlist)
        mapped_irlist = irlist_append(mapped_irlist, make_irlist(func(first)))
        irlist = irlist_rest(irlist)
    return mapped_irlist


def irlist_str(irlist):
    """Return a string representation for irlist.

    >>> irlist_str(irlist_populate(1, 2, 3, 4, 5))
    '<1, 2, 3, 4, 5>'
    >>> irlist_str(empty_irlist)
    '<>'
    >>> irlist_str(irlist_populate(irlist_populate(1, 2), 3))
    '<<1, 2>, 3>'
    """
    result = "<"
    while irlist != empty_irlist:
        if could_be_irlist(irlist_first(irlist)):
            result += irlist_str(irlist_first(irlist))
        else:
            result += repr(irlist_first(irlist))
        # Move forward and add comma if necessary
        irlist = irlist_rest(irlist)
        if irlist != empty_irlist:
            result += ", "
    return result + ">"
