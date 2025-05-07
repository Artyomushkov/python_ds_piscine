import sys
from ft_filter import my_filter


def main():
    """
    Filters words from a given string based on their length.
    The function takes two command-line arguments:
    1. A string of words separated by spaces.
    2. An integer representing the minimum word length.
    """
    try:
        if len(sys.argv) != 3:
            raise AssertionError("more than one argument is provided")
        str_length = int(sys.argv[2])
        str_list = sys.argv[1].split()
        print(list(my_filter(lambda word: len(word) > str_length, str_list)))
    except Exception:
        print("AssertionError: the arguments are bad")
        return


if __name__ == "__main__":
    main()
