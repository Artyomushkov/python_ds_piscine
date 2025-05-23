def my_filter(func, iterable):
    """filter(function or None, iterable) --> filter object

    Return an iterator yielding those items of iterable
    for which function(item) is true.
    If function is None, return the items that are true."""
    if func:
        return (item for item in iterable if func(item))
    return (item for item in iterable if item)
