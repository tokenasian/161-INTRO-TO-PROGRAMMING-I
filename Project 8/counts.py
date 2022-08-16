# Author: Matthew Armstrong
# Date: 7/25/21
# Description: returns a dictionary
# that tabulates how many of each letter is in that string.
def count_letters(string):
    """dictionary stores letter frequency in string"""
    letter_dict = {}
    for i in string.upper():
        is_letter = True
        if i.upper() == i.lower():
            is_letter = False
        if not is_letter:
            continue
        if i in letter_dict:
            letter_dict[i] += 1
        else:
            letter_dict[i] = 1
    return letter_dict
