import sys


def main():
    """
    Count the number of upper and lower case letters, punctuation marks,
    spaces, and digits in a given string.
    """
    if len(sys.argv) > 2:
        print("AssertionError: more than one argument is provided")
        return
    count_str = ""
    if len(sys.argv) == 1:
        count_str = input("What is the text to count?\n")
    else:
        count_str = sys.argv[1]
    uppers = 0
    lowers = 0
    punctuationMarks = 0
    spaces = 0
    digits = 0
    for char in count_str:
        if char.isupper():
            uppers += 1
        elif char.islower():
            lowers += 1
        elif char.isspace():
            spaces += 1
        elif char.isdigit():
            digits += 1
        else:
            punctuationMarks += 1
    print(f"The text contains {len(count_str)} characters:\n" +
          f"{uppers} upper letters\n" +
          f"{lowers} lower letters\n" +
          f"{punctuationMarks} punctuation marks\n" +
          f"{spaces} spaces\n" +
          f"{digits} digits")


if __name__ == "__main__":
    main()
