# Python String 113 exercises

        #  1. Write a Python program to calculate the length of a string.
ex1 = str(input('Enter the string: '))
print(len(ex1))

        #  2. Write a Python program to count the number of characters (character frequency) in a string.
        # Sample String : google.com'
        # Expected Result : {'g': 2, 'o': 3, 'l': 1, 'e': 1, '.': 1, 'c': 1, 'm': 1}
ex2 = str(input('Enter the string: '))
ex2_freq = {}
for a in ex2:
    if a in ex2_freq:
        ex2_freq[a] += 1
    else:
        ex2_freq[a] = 1
print(ex2_freq)

        #  3. Write a Python program to get a string made of the first 2 and last 2 characters of a given string. If the string length is less than 2, return the empty string instead.
        # Sample String : 'w3resource'
        # Expected Result : 'w3ce'
        # Sample String : 'w3'
        # Expected Result : 'w3w3'
        # Sample String : ' w'
        # Expected Result : Empty String
ex3 = str(input('Enter the string: '))
if len(ex3) > 1:
    print(ex3[:2] + ex3[-2:])
else:
    print('')


        #  4. Write a Python program to get a string from a given string where all occurrences of its first char have been changed to '$', except the first char itself.
        # Sample String : 'restart'
        # Expected Result : 'resta$t'
ex4 = str(input('Enter the string: '))
result_ex4 = ex4[0] + ex4[1:].replace(ex4[0], '$')
print(result_ex4)

        #  5. Write a Python program to get a single string from two given strings, separated by a space and swap the first two characters of each string.
        # Sample String : 'abc', 'xyz'
        # Expected Result : 'xyc abz'
ex5_a = str(input('Enter the 1st string: '))
ex5_b = str(input('Enter the 2nd string: '))

result_ex5 = ex5_b[:2] + ex5_a[2:] + " " + ex5_a[:2] + ex5_b[2:]

print(result_ex5)


        #  6. Write a Python program to add 'ing' at the end of a given string (length should be at least 3). If the given string already ends with 'ing', add 'ly' instead. If the string length of the given string is less than 3, leave it unchanged.
        # Sample String : 'abc'
        # Expected Result : 'abcing'
        # Sample String : 'string'
        # Expected Result : 'stringly'
ex6 = str(input('Enter the string: '))
if len(ex6) >= 3 and ex6[-3:] == 'ing':
    print(ex6 + 'ly')
elif len(ex6) >= 3 and ex6[-3:] != 'ing':
    print(ex6 + 'ing')
else:
    print(ex6)

        #  7. Write a Python program to find the first appearance of the substrings 'not' and 'poor' in a given string. If 'not' follows 'poor', replace the whole 'not'...'poor' substring with 'good'. Return the resulting string.
        # Sample String : 'The lyrics is not that poor!'
        # 'The lyrics is good!'
        # Expected Result : 'The lyrics is poor!'
        # 'The lyrics is poor!'
ex7 = str(input('Enter the string: '))
ex7_not = ex7.find('not')
ex7_poor = ex7.find('poor')
if ex7_not != -1 and ex7_poor != -1 and ex7_not < ex7_poor:
    result_ex7 = ex7[:ex7_not] + 'good' + ex7[ex7_poor + 4:]
else:
    result_ex7 = ex7
print(result_ex7)


        #  8. Write a Python function that takes a list of words and return the longest word and the length of the longest one.
        # Sample Output:
        # Longest word: Exercises
        # Length of the longest word: 9
ex8 = str(input('Enter the string: '))
ex8_words = ex8.split()
print(max(ex8_words, key=len))

        #  9. Write a Python program to remove the nth index character from a nonempty string.
ex9_string = str(input('Enter the string: '))
ex9_index = int(input('Enter the index to remove: '))
result_ex9 = ex9_string[:ex9_index] + ex9_string[ex9_index + 1:]
print(result_ex9)

        #  10. Write a Python program to change a given string to a new string where the first and last chars have been exchanged.
ex10 = str(input('Enter the string: '))
if len(ex10) < 2:
    result_ex10 = ex10
else:
    result_ex10 = ex10[-1] + ex10[1:-1] + ex10[0]
print(result_ex10)

        #  11. Write a Python program to remove characters that have odd index values in a given string.
ex11 = str(input('Enter the string: '))
result_ex11 = ex11[::2]
print(result_ex11)

        #  12. Write a Python program to count the occurrences of each word in a given sentence.
ex12 = str(input('Enter the string: '))
ex12_words = ex12.split()
ex12_counts = {}
for b in ex12_words:
    ex12_counts[b] = ex12_counts.get(b, 0) + 1
print(ex12_counts)

        #  13. Write a Python script that takes input from the user and displays that input back in upper and lower cases.
ex13 = str(input('Enter the string: '))
print(ex13.upper())
print(ex13.lower())

        #  14. Write a Python program that accepts a comma-separated sequence of words as input and prints the distinct words in sorted form (alphanumerically).
        # Sample Words : red, white, black, red, green, black
        # Expected Result : black, green, red, white,red
ex14 = str(input('Enter the string with comma: '))
ex14_words = ex14.split(',')
ex14_distinct = sorted(set(ex14_words))
print(','.join(ex14_distinct))

        #  15. Write a Python function to create an HTML string with tags around the word(s).
        # Sample function and result :
        # add_tags('i', 'Python') -> '<i>Python</i>'
        # add_tags('b', 'Python Tutorial') -> '<b>Python Tutorial </b>'
ex15_tag = str(input('Enter the tag: '))
ex15_string = str(input('Enter the string: '))
print(f'<{ex15_tag}>{ex15_string}</{ex15_tag}>')

        #  16. Write a Python function to insert a string in the middle of a string.
        # Sample function and result :
        # insert_sting_middle('[[]]<<>>', ' Python') -> [[Python]]insert_sting_middle('{{}}', 'PHP') -> {{PHP}}
ex16_container = str(input('Enter the container string: '))
ex16_insert = str(input('Enter the string to insert: '))
ex16_middle = len(ex16_container) // 2
result_ex16 = ex16_container[:ex16_middle] + ex16_insert + ex16_container[ex16_middle:]
print(result_ex16)

        #  17. Write a Python function to get a string made of 4 copies of the last two characters of a
        # specified string (length must be at least 2).
        # Sample function and result :
        # insert_end('Python') -> onononon
        # insert_end('Exercises') -> eseseses
ex17 = str(input('Enter the string (min length 2: '))
result_ex17 = ex17[-2] * 4
print(result_ex17)

        #  18. Write a Python function to get a string made of the first three characters of a specified string.
        # If the length of the string is less than 3, return the original string.
        # Sample function and result :
        # first_three('ipy') -> ipy
        # first_three(' python') -> pyt
ex18 = str(input('Enter the string: '))
if len(ex18) > 3:
    result_ex18 = ex18[:3]
    print(result_ex18)
else:
    print(ex18)

        #  19. Write a Python program to get the last part of a string before a specified character.
        # https://www.w3resource.com/python-exercises
        # https://www.w3resource.com/python
ex19 = str(input('Enter the string: '))
ex19_char = input('Enter a character: ')
result_ex19 = ex19.rsplit(ex19_char, 1)[0]
print(result_ex19)

        #  20. Write a Python function to reverse a string if its length is a multiple of 4.
ex20 = str(input('Enter the string: '))
if len(ex20) % 4 == 0:
    ex20 = ex20[::-1]
print(ex20)

        #  21. Write a Python function to convert a given string to all uppercase if it contains at least 2 uppercase characters in the first 4 characters.
ex21 = str(input('Enter the string: '))
ex21_first_four_chars = ex21[:4]
ex21_uppercase_count = 0
for c in ex21_first_four_chars:
    if c.isupper():
        ex21_uppercase_count +=1
if ex21_uppercase_count >= 2:
    ex21 = ex21.upper()
print(ex21)

        #  22. Write a Python program to sort a string lexicographically.
ex22 = str(input('Enter the string: '))
print(''.join(sorted(ex22)))

        #  23. Write a Python program to remove a newline in Python.
ex23 = "New\nLine"
print(ex23.replace('\n',''))

        #  24. Write a Python program to check whether a string starts with specified characters.
ex24 = str(input('Enter the string: '))
ex24_start = input('Enter specific character(s): ')
print(ex24.startswith(ex24_start))

        # 25. Write a Python program to create a Caesar encryption.
        # Note : In cryptography, a Caesar cipher, also known as Caesar's cipher, the shift cipher, Caesar's code or Caesar shift, is one of the simplest and most widely known encryption techniques. It is a type of substitution cipher in which each letter in the plaintext is replaced by a letter some fixed number of positions down the alphabet. For example, with a left shift of 3, D would be replaced by A, E would become B, and so on. The method is named after Julius Caesar, who used it in his private correspondence.
ex25_text = input('Enter the string: ')
ex25_shift = int(input('Enter the shift value: '))
ex25_encrypted = ''
for d in ex25_text:
    if d.isalpha():
        ex25_base = ord('A') if d.isupper() else ord('a')

        ex25_encrypted += chr((ord(d) - ex25_base + ex25_shift) % 26 + ex25_base)
    else:
        ex25_encrypted += d
print('Caesar encryption: ', ex25_encrypted)

        # 26. Write a Python program to display formatted text (width=50) as output.
import textwrap
ex26 = input('Enter the string: ')
print(textwrap.fill(ex26, width = 50))

        # 27. Write a Python program to remove existing indentation from all the lines in a given text.
import textwrap
ex27 = input('Enter text with indentation:\n')
print(textwrap.dedent(ex27))

        # 28. Write a Python program to add prefix text to all the lines in a string.
ex28 = input('Enter multiple lines (use \\n to separate):\n')
print('\n'.join('>> ' + line for line in ex28.splitlines()))

        # 29. Write a Python program to set the indentation of the first line.
ex29 = input('Enter the string: ')
print(' ' + ex29.replace('\n','\n'))

        # 30. Write a Python program to print the following numbers up to 2 decimal places.
ex30 = float(input('Enter a number: '))
print('{:.2f}'.format(ex30))

        # 31. Write a Python program to print the following numbers up to 2 decimal places with a sign.
ex31 = float(input('Enter a number: '))
print('{:+.2f}'.format(ex31))

        # 32. Write a Python program to print the following positive and negative numbers with no decimal places.
ex32 = float(input('Enter a number: '))
print('{:.0f}'.format(ex32))

        # 33. Write a Python program to print the following integers with zeros to the left of the specified width.
ex33 = int(input('Enter an integer: '))
print('{:05d}'.format(ex33))

        # 34. Write a Python program to print the following integers with '*' to the right of the specified width.
ex34 = int(input('Enter an integer: '))
print('{:*<5d}'.format(ex34))

        # 35. Write a Python program to display a number with a comma separator.
ex35 = int(input('Enter a number: '))
print('{:,}'.format(ex35))

        # 36. Write a Python program to format a number with a percentage.
ex36 = float(input('Enter a decimal: '))
print('{:.2%}'.format(ex36))

        # 37. Write a Python program to display a number in left, right, and center aligned with a width of 10.
ex37 = input('Enter the string: ')
print('{:<10}'.format(ex37))
print('{:>10}'.format(ex37))
print('{:^10}'.format(ex37))

        # 38. Write a Python program to count occurrences of a substring in a string.
ex38 = str(input('Enter the string: '))
ex38_sub = str(input('Enter the substring to count: '))
print(ex38.count(ex38_sub))

        # 39. Write a Python program to reverse a string.
ex39 = str(input('Enter the string: '))
print(ex39[::-1])

        # 40. Write a Python program to reverse words in a string.
ex40 = str(input('Enter the sentence: '))
print(' '.join(ex40.split()[::-1]))

        # 41. Write a Python program to strip a set of characters from a string.
ex41 = str(input('Enter the string: '))
ex41_chars = input('Enter characters to remove: ')
result_ex41 = ''.join(e for e in ex41 if e not in ex41_chars)
print(result_ex41)

        # 42. Write a Python program to count repeated characters in a string.
        # Sample string: 'thequickbrownfoxjumpsoverthelazydog'
        # Expected output :
        # o 4
        # e 3
        # u 2
        # h 2
        # r 2
        # t 2
ex42 = str(input('Enter the string: '))
ex42_counts = {}
for f in ex42:
    ex42_counts[f] = ex42_counts.get(f,0) + 1
for g,h in ex42_counts.items():
    if h > 1:
        print(g, h)

        # 43. Write a Python program to print the square and cube symbols in the area of a rectangle and the volume of a cylinder.
        # Sample output:
        # The area of the rectangle is 1256.66cm2
        # The volume of the cylinder is 1254.725cm3
import math
ex43_length = float(input('Enter length of rectangle: '))
ex43_width = float(input('Enter width of rectangle: '))
ex43_radius = float(input('Enter radius of cylinder: '))
ex43_height = float(input('Enter height of cylinder: '))

ex43_area = ex43_length * ex43_width
ex43_volume = math.pi * ex43_radius**2 * ex43_height
print (f'The area of the rectangle is {ex43_area:.2f}cm\u00b2')
print (f'The volume of the cylinder is {ex43_volume:.3f}cm\u00b3')

        # 44. Write a Python program to print the index of a character in a string.
        # Sample string: w3resource
        # Expected output:
        # Current character w position at 0
        # Current character 3 position at 1
        # Current character r position at 2
        # - - - - - - - - - - - - - - - - - - - - - - - - -
        # Current character c position at 8
        # Current character e position at 9
ex44 = str(input('Enter the string: '))
for i, j in enumerate(ex44):
    print(f'Current character {j} position at {i}')

        # 45. Write a Python program to check whether a string contains all letters of the alphabet.
import string
ex45 = str(input('Enter the string: ').lower())
ex45_alphabet = set(string.ascii_lowercase)

if ex45_alphabet <= set(ex45):
    print('The string contains all letters of the alphabet.')
else:
    print('The string does NOT contain all letters of the alphabet.')

        # 46. Write a Python program to convert a given string into a list of words.
        # Sample Output:
        # ['The', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog.']
        # ['The', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog.']
ex46 = str(input('Enter a sentence: '))
ex46_words = ex46.split()
print(ex46_words)

        # 47. Write a Python program to lowercase the first n characters in a string.
ex47 = str(input('Enter the string: '))
ex47_n = int(input('Enter n: '))
result_ex47 = ex47[:ex47_n].lower() + ex47[ex47_n:]
print(result_ex47)

        # 48. Write a Python program to swap commas and dots in a string.
        # Sample string: "32.054,23"
        # Expected Output: "32,054.23"
ex48 = str(input('Enter the string: '))
result_ex48 = ex48.replace('.', 'TEMP').replace(',','.').replace('TEMP',',')
print(result_ex48)

        # 49. Write a Python program to count and display vowels in text.
ex49 = str(input('Enter the string: ').lower())
ex49_vowels = 'aeiou'
for k in ex49_vowels:
    ex49_count = ex49.count(k)
    if ex49_count > 0:
        print(k, ex49_count)

        # 50. Write a Python program to split a string on the last occurrence of the delimiter.
ex50 = str(input('Enter the string: '))
ex50_delimeter = str(input('Enter a delimeter: '))
ex50_parts = ex50.rsplit(ex50_delimeter, 1)
print(ex50_parts)
