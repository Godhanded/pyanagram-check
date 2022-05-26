# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagram(word, anagram):
    # [assignment] Add your code here
    if len(word)==len(anagram):
       word = word.strip().lower()
       anagram = anagram.strip().lower()
       word = sorted(word)
       anagram = sorted(anagram)
    
       if word !=anagram:
           return False
       return True
    else:
        return False            


print (find_anagram(input("input word \n"), input("input anagram \n")))
