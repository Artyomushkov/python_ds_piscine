def count_in_list(lst, obj):
    """
    Count the number of occurrences of the object in a list.

    Args:
        lst (list): The list to search.
        obj (str): The object to count.
    """
    count = 0
    for item in lst:
        if item == obj:
            count += 1
    return count
