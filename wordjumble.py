"""wordjumble.py

Can you create a program to solve a word jumble? The
program should accept a string as input, and then return a list of
words that can be created using the submitted letters. For example, on
the input "dog", the program should return a set of words including
"god", "do", and "go".

This program accepts a string of characters (one string) and outputs a list
of valid English words that can be formed by the characters in the input.

Call like this:
    python wordjumble.py input_string

Files:
  wordjumble.py - The program itself
  wordjumble_tests.py - Unit tests for the program
  wordsEn.txt - A word dictionary from http://www-01.sil.org/linguistics/wordlists/english/

Word List: 
We access the word list one line at a time and check if the
word is possible before moving on to the next word. This is memory
efficient, fast, and leads to simple code.  From this perspective, the
runtime of the program is limited by disk access. O(n) disk accesses
are made by the program, where n is the length of the word list. The
speedup gained by reading the whole word list into memory first is
insignificant.

Testing for containment: 
We test every dictionary word to see if it
can be formed using the letters provided to us in the jumble. This
takes O(nlogn) time per test as we sort the dictionary word in order
to perform an O(n) comparison with the jumbled word (which we sort
once beforehand).  In this case, n is the size of the longest
dictionary word. If there are O(M) words in the dictionary file, the
entire operation is O(M.nlogn). Since M is much larger than n,
it dominates the runtime, and so the entire operation is much closer
to O(M). 
"""

dict_file = 'wordsEn.txt'

def find_valid_words(jumbled_word):
    """Iterates through every word in our dictionary and
    outputs a list that can be contained in the jumbled word.
    """
    b = sorted(jumbled_word)
    matches = []
    with open(dict_file, 'r') as word_list:
        for word in word_list:
            w = word.strip()
            if contains(w, b):
                matches.append(w)
                print w
        return matches

def contains(a, b):
    """Returns true if a is contained in b.
    Containment is defined as follows: 
    a is said to be contained in b, if, b contains exactly all the letters in a (this
    includes duplicates).
    b is assumed to already be sorted.
    """
    if len(a) > len(b):
        return False
    a = "".join(sorted(a))
    
    a_i = 0
    b_i = 0
    while a_i < len(a) and b_i < len(b):
        if a[a_i] == b[b_i]:
            a_i += 1
            b_i += 1
        else:
            b_i += 1
        
    if a_i == len(a):
        return True
    else:
        return False

def help():
    print "Welcome to wordjumble."
    print "This program accepts input in the form of one string."
    print "Ex. python wordjumble.py foobar"

import sys, pprint
def main():
    if len(sys.argv) != 2:
        print "Invalid arguments."
        help()
        return
    
    #pprint.pprint(find_valid_words(sys.argv[1]))
    find_valid_words(sys.argv[1])

if __name__ == '__main__':
    main()

