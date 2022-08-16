# Author: Matthew Armstrong
# Date: 7/25/21
# Description: returns a set of words that appear in only both strings
def words_in_both(s1, s2):
    """returns a set of words that appear in only both strings"""
    string1 = set(s1.lower().split())
    string2 = set(s2.lower().split())
    return string1.intersection(string2)
