"""
Problem Statement
Count total vowels in a given sentence (case-insensitive).
Input
sentence
Output
vowel_count

Sample Input
I Love Python
Sample Output
4

Hint:
Normalize case before comparison.

"""
def count_vowels(sentence):
    vowels = ['a', 'e', 'i', 'o', 'u']
    count = 0
    for char in sentence:
        if char in vowels:
            count += 1
    return count

sentence = input().lower()
print(count_vowels(sentence))