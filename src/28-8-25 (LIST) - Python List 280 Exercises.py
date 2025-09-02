        # 1. Write a Python program to sum all the items in a list.
ex1 = input('Enter numbers separated by space: ').split()
ex1_convert = []

for a in ex1:
    ex1_convert.append(int(a))

print("Sum of all numbers: ", sum(ex1_convert))

        # 2. Write a Python program to multiply all the items in a list.
ex2 = input('Enter numbers separated by space: ').split()
ex2_convert = []

for b in ex2:
    ex2_convert.append(int(b))

ex2_base = 1
for b_base in ex2_convert:
    ex2_base *= b_base

print('Multiplication of all numbers: ', ex2_base)

        # 3. Write a Python program to get the largest number from a list.
ex3 = input('Enter numbers separated by space: ').split()
ex3_convert = []

for c in ex3:
    ex3_convert.append(int(c))

print('Largest number: ', max(ex3_convert))

        # 4. Write a Python program to get the smallest number from a list.
ex4 = input('Enter numbers separated by space: ').split()
ex4_convert = []

for d in ex4:
    ex4_convert.append(int(d))

print('Smallest number: ', min(ex4_convert))

        # 5. Write a Python program to count the number of strings from a given list of strings. The string length is 2 or more and the first and last characters are the same.
        # Sample List : ['abc', 'xyz', 'aba', '1221']
        # Expected Result : 2
ex5 = input('Enter words separated by space: ').split()

ex5_base = 0
for e in ex5:
    if len(e) >= 2 and e[0] == e[-1]:
        ex5_base += 1

print('Count: ', ex5_base)

        # 6. Write a Python program to get a list, sorted in increasing order by the last element in each tuple from a given list of non-empty tuples.
        # Sample List : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
        # Expected Result : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]
ex6 = input('Enter tuples like 2,5 1,2 4,4: ').split()
ex6_tuples = []

for f in ex6:
    g, h = f.split(',')
    ex6_tuples.append((int(g), int(h)))

print('Sorted list in increasing order by the last element: ', sorted(ex6_tuples, key=lambda i: i[-1]))

        # 7. Write a Python program to remove duplicates from a list.
ex7 = input('Enter numbers (with duplicates): ').split()
ex7_convert = []
for j in ex7:
    ex7_convert.append(int(j))

ex7_unique_no_order = []
for k in ex7_convert:
    if k not in ex7_unique_no_order:
        ex7_unique_no_order.append(k)

ex7_unique_order = list(set(ex7_convert))

print('List without duplicates (not in order): ', ex7_unique_no_order)
print('List without duplicates (in order): ', ex7_unique_order)

        # 8. Write a Python program to check if a list is empty or not.
ex8 = input('Enter items (leave blank for empty list): ').split()
if not ex8:
    print('The list is empty.')
else:
    print('The list is not empty.')

        # 9. Write a Python program to clone or copy a list.
ex9 = input('Enter list items: ').split()
ex9_clone = ex9.copy()
print('Clone list: ', ex9_clone)

        # 10. Write a Python program to find the list of words that are longer than n from a given list of words.
ex10 = input('Enter words separated by space: ').split()
ex10_n = int(input('Enter n: '))

ex10_longer_words = []
for l in ex10:
    if len(l) > ex10_n:
        ex10_longer_words.append(l)

print('Words longer than', ex10_n, ': ', ex10_longer_words)

        # 11. Write a Python function that takes two lists and returns True if they have at least one common member.
ex11_list_1 = input('Enter the first list items: ').split()
ex11_list_2 = input('Enter the second list items: ').split()

ex11_common = False
for m in ex11_list_1:
    if m in ex11_list_2:
        ex11_common = True
        break

print('Have common member:', ex11_common)

        # 12. Write a Python program to print a specified list after removing the 0th, 4th and 5th elements.
        # Sample List : ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
        # Expected Output : ['Green', 'White', 'Black']
ex12 = input('Enter the list items: ').split()
ex12_specified_list = []

for n in range(len(ex12)):
    if n not in (0,4,5):
        ex12_specified_list.append(ex12[n])

print('After removing the 0th, 4th and 5th elements: ', ex12_specified_list)

        # 13. Write a Python program to generate a 3*4*6 3D array who's each element is *.
ex13 = []
for o in range(3):
    ex13_block = []
    for p in range(4):
        ex13_row = []
        for q in range(6):
            ex13_row.append('*')
        ex13_block.append(ex13_row)
    ex13.append(ex13_block)

for ex13_depth, ex13_block in enumerate(ex13):
    print(f'Block {ex13_depth + 1}: ')
    for ex13_row in ex13_block:
        print(ex13_row)
    print()

        # 14. Write a Python program to print the numbers of a specified list after removing even numbers from it.
ex14 = input('Enter numbers separated by space: ').split()
ex14_convert = []
for r in ex14:
    ex14_convert.append(int(r))

ex14_specified_list = []
for s in ex14_convert:
    if s % 2 != 0:
        ex14_specified_list.append(s)

print('After removing even numbers: ', ex14_specified_list)

        # 15. Write a Python program to shuffle and print a specified list.
import random

ex15 = input('Enter list items: ').split()
random.shuffle(ex15)
print('Shuffled list: ', ex15)

        # 16. Write a Python program to generate and print a list of the first and last 5 elements where the values are square numbers between 1 and 30 (both included).
ex16_squares = []
for t in range(1,31):
    ex16_squares.append(t*t)

ex16 = ex16_squares[:5] + ex16_squares[-5:]
print('First and last 5 squares: ', ex16)

        # 17. Write a Python program to check if each number is prime in a given list of numbers. Return True if all numbers are prime otherwise False.
        # Sample Data:
        # ([0, 3, 4, 7, 9]) -> False
        # ([3, 5, 7, 13]) -> True
        # ([1, 5, 3]) -> False
ex17 = input('Enter numbers separated by space: ').split()
ex17_convert = []
for u in ex17:
    ex17_convert.append(int(u))

ex17_prime = True

for ex17_numbers in ex17_convert:
    if ex17_numbers < 2:
        ex17_prime = False
        break

    for v in range(2, int(ex17_numbers ** 0.5) + 1):
        if ex17_numbers % v == 0:
            ex17_prime = False
            break
    if not ex17_prime:
        break

print('All numbers are prime:', ex17_prime)

        # 18. Write a Python program to generate all permutations of a list in Python.
import itertools

ex18 = input('Enter the list items: ').split()
ex18_permutation = list(itertools.permutations(ex18))

print('All permutations: ')
for w in ex18_permutation:
    print(w)

        # 19. Write a Python program to calculate the difference between the two lists.
ex19_list_1 = input('Enter first list items: ').split()
ex19_list_2 = input('Enter second list items: ').split()
ex19_difference = []

for ex19_item in ex19_list_1:
    if ex19_item not in ex19_list_2:
        ex19_difference.append(ex19_item)

for ex19_item in ex19_list_2:
    if ex19_item not in ex19_list_1:
        ex19_difference.append(ex19_item)

print('Difference between lists:', ex19_difference)

        # 20. Write a Python program to access the index of a list.
ex20 = input('Enter list items: ').split()
for y in range(len(ex20)):
    print('Index:', y, 'Value:', ex20[y])

        # 21. Write a Python program to convert a list of characters into a string.
ex21 = input('Enter characters separated by space: ').split()
ex21_string = ''.join(ex21)
print('String:', ex21_string)

        # 22. Write a Python program to find the index of an item in a specified list.
ex22 = input('Enter list items: ').split()
ex22_item = input('Enter item to find index: ')
if ex22_item in ex22:
    print('Index of', ex22_item, 'is:', ex22.index(ex22_item))
else:
    print('Item not found in list.')

        # 23. Write a Python program to flatten a shallow list.
ex23 = input("Enter sublists separated by ';' (use space inside sublist): ").split(';')
ex23_list_of_lists = []
for ex23_sub in ex23:
    ex23_items = ex23_sub.strip().split()
    ex23_list_of_lists.append(ex23_items)

print('Original list of lists:', ex23_list_of_lists)

ex23_flattened_list = []
for ex23_sublist in ex23_list_of_lists:
    for ex23_item in ex23_sublist:
        ex23_flattened_list.append(ex23_item)

print('Flattened list:', ex23_flattened_list)

        # 24. Write a Python program to append a list to the second list.
ex24_list_1 = input('Enter first list items: ').split()
ex24_list_2 = input('Enter second list items: ').split()
ex24_list_1.extend(ex24_list_2)
print('Combined list:', ex24_list_1)

        # 25. Write a Python program to select an item randomly from a list.
import random

ex25 = input('Enter list items: ').split()
ex25_random = random.choice(ex25)
print('Random selected items:', ex25_random)

        # 26. Write a Python program to check whether two lists are circularly identical.
ex26_list_1 = input('Enter first list items: ').split()
ex26_list_2 = input('Enter second list items: ').split()

print('List 1:', ex26_list_1)
print('List 2:', ex26_list_2)

if len(ex26_list_1) != len(ex26_list_2):
    print('The lists are not circularly identical.')
else:
    ex26_doubled = ex26_list_1 + ex26_list_1

    if any(ex26_doubled[z: z + len(ex26_list_2)] == ex26_list_2 for z in range(len(ex26_list_1))):
        print('The list are circularly identical.')
    else:
        print('The list are not circularly identical.')

        # 27. Write a Python program to find the second-smallest number in a list.
ex27 = input('Enter numbers (space separated): ').split()

ex27_num = []
for a1 in ex27:
    ex27_num.append(int(a1))
print('Original list:', ex27_num)

ex27_num.sort()
ex27_second_smallest = ex27_num[1]
print('Second smallest number:', ex27_second_smallest)

        # 28. Write a Python program to find the second-largest number in a list.
ex28 = input('Enter numbers (space separated): ').split()

ex28_num = []
for b1 in ex28:
    ex28_num.append(int(b1))
print('Original list:', ex28_num)

ex28_num.sort()
ex28_second_largest = ex28_num[-2]
print('Second largest number:', ex28_second_largest)

        # 29. Write a Python program to get unique values from a list.
ex29 = input('Enter list items: ').split()
ex29_unique = list(set(ex29))
print('Unique values: ', ex29_unique)

        # 30. Write a Python program to get the frequency of elements in a list.
ex30 = input('Enter list items: ').split()
ex30_frequency = {}
for ex30_item in ex30:
    if ex30_item in ex30_frequency:
        ex30_frequency[ex30_item] += 1
    else:
        ex30_frequency[ex30_item] = 1
print('Frequency of elements:', ex30_frequency)

        # 31. Write a Python program to count the number of elements in a list within a specified range.
ex31 = input('Enter numbers (space separated): ').split()

ex31_num = []
for c1 in ex31:
    ex31_num.append(int(c1))
print('Original list:', ex31_num)

ex31_lower = int(input('Enter lower bound: '))
ex31_upper = int(input('Enter upper bound: '))

ex31_count = 0
for c1 in ex31_num:
    if ex31_lower <= c1 <= ex31_upper:
        ex31_count += 1
print('Number of elements within range:', ex31_count)

        # 32. Write a Python program to check whether a list contains a sublist.
ex32_main_list = input('Enter main list items (space separated): ').split()
ex32_sub_list = input('Enter sub list items (space separated): ').split()

print('Main list:', ex32_main_list)
print('Sublist:', ex32_sub_list)

ex32_found = False
for d1 in range(len(ex32_main_list) - len(ex32_sub_list) + 1):
    if ex32_main_list[d1: d1 + len(ex32_sub_list)] == ex32_sub_list:
        ex32_found = True
        break

if ex32_found:
    print('The sublist is contained in the main list.')
else:
    print('The sublist is not contained in the main list.')

        # 33. Write a Python program to generate all sublists of a list.
ex33 = input('Enter list items: ').split()
ex33_sublist = [[]]

for e1 in range(len(ex33)):
    for f1 in range(e1 + 1, len(ex33) + 1):
        ex33_sublist.append(ex33[e1 : f1])

print('All sublists:', ex33_sublist)

        # 34. Write a Python program that uses the Sieve of Eratosthenes method to compute prime numbers up to a specified number.
        # Note: In mathematics, the sieve of Eratosthenes, (Ancient Greek: κόσκινον Ἐρατοσθένους, kóskinon Eratosthénous) one of a number of prime number sieves, is a simple, ancient algorithm for finding all prime numbers up to any given limit.
ex34 = int(input('Find primes up to: '))
ex34_primes = [True] * (ex34 + 1)
ex34_primes[0] = ex34_primes[1] = False

for g1 in range(2, int(ex34 ** 0.5) + 1):
    if ex34_primes[g1]:
        for h1 in range(g1 * g1, ex34 + 1, g1):
            ex34_primes[h1] = False

ex34_prime_numbers = [g1 for g1 in range(ex34 + 1) if ex34_primes[g1]]

print('Prime numbers up to', ex34, ':', ex34_prime_numbers)

        # 35. Write a Python program to create a list by concatenating a given list with a range from 1 to n.
        # Sample list : ['p', 'q']
        # n =5
        # Sample Output : ['p1', 'q1', 'p2', 'q2', 'p3', 'q3', 'p4', 'q4', 'p5', 'q5']
ex35 = input('Enter list items (space separated): ').split()
i1 = int(input('Enter n (the range end number): '))
print('Base list:', ex35)
ex35_result = []
for j1 in range(1, i1+1):
    for ex35_item in ex35:
        ex35_result.append(ex35_item + str(j1))
print('Concatenated list:', ex35_result)

        # 36. Write a Python program to get a variable with an identification number or string.
ex36 = input('Enter a value (number or string): ')
print('Value:', ex36)
print('ID of variable:', id(ex36))

        # 37. Write a Python program to find common items in two lists.
ex37_list_1 = input('Enter the first list items: ').split()
ex37_list_2 = input('Enter the second list items: ').split()
ex37_common = list(set(ex37_list_1) & set(ex37_list_2))
print('Common items:', ex37_common)

        # 38. Write a Python program to change the position of every n-th value to the (n+1)th in a list.
        # Sample list: [0,1,2,3,4,5]
        # Expected Output: [1, 0, 3, 2, 5, 4]
ex38 = input('Enter numbers separated by space: ').split()
ex38 = [int(k1) for k1 in ex38]

print('Original list:', ex38)

for l1 in range(0, len(ex38) -1, 2):
    ex38[l1], ex38[l1 + 1] = ex38[l1 + 1], ex38[l1]

print('Swapped list:', ex38)

        # 39. Write a Python program to convert a list of multiple integers into a single integer.
        # Sample list: [11, 33, 50]
        # Expected Output: 113350
ex39 = input('Enter numbers separated by space: ').split()
ex39_str = ''.join(ex39)
ex39_integer = int(ex39_str)
print('Single integer:', ex39_integer)

        # 40. Write a Python program to split a list based on the first character of a word.
ex40 = input('Enter words separated by space: ').split()

ex40_result = {}
for ex40_word in ex40:
    ex40_key = ex40_word[0]
    if ex40_key not in ex40_result:
        ex40_result[ex40_key] = []
    ex40_result[ex40_key].append(ex40_word)

print('Split by first character:', ex40_result)

        # 41. Write a Python program to create multiple lists.
ex41 = int(input('How many lists do you want to create? '))
ex41_list = []

for m1 in range(ex41):
    ex41_raw = input(f'Enter items for list {m1 + 1} (separated by space): ')
    ex41_new = ex41_raw.split()
    ex41_list.append(ex41_new)

print('All created lists: ')
for ex41_index, n1 in enumerate(ex41_list, start = 1):
    print(f'List {ex41_index}:', 1)

        # 42. Write a Python program to find missing and additional values in two lists.
        # Sample data : Missing values in second list: b,a,c
        # Additional values in second list: g,h
ex42_list_1 = input('Enter first list: ').split()
ex42_list_2 = input('Enter second list: ').split()

ex42_missing = list(set(ex42_list_1) - set(ex42_list_2))
ex42_additional = list(set)

        # 43. Write a Python program to split a list into different variables.
ex43 = input('Enter items: ').split()

ex43_a, ex43_b, ex43_c = ex43[:3]

print('a =', ex43_a)
print('b =', ex43_b)
print('c =', ex43_c)

        # 44. Write a Python program to generate groups of five consecutive numbers in a list.
ex44 = int(input('Enter how many groups of 5 you want: '))
ex44_result = []

for o1 in range(ex44):
    ex44_start = o1 * 5
    ex44_group = list(range(ex44_start, ex44_start + 5))
    ex44_result.append(ex44_group)

print('Group of five consecutive numbers: ')
for p1 in ex44_result:
    print(p1)

        # 45. Write a Python program to convert a pair of values into a sorted unique array.
ex45 = input('Enter two values separated by space: ').split()
ex45 = [int(q1) for q1 in ex45]

ex45_sort = sorted(set(ex45))

print('Sorted unique array:', ex45_sort)

        # 46. Write a Python program to select the odd items from a list.
ex46 = input('Enter numbers: ').split()
ex46 = [int(r1) for r1 in ex46]

ex46_odd = [r1 for r1 in ex46 if r1 % 2 != 0]

print('Odd items:', ex46_odd)

        # 47. Write a Python program to insert an element before each element of a list.
ex47 = input('Enter list items: ').split()
ex47_insert = input('Enter element to insert before each item: ')

ex47_result = []
for ex47_item in ex47:
    ex47_result.append(ex47_insert)
    ex47_result.append(ex47_item)

print('Result:', ex47_result)

        # 48. Write a Python program to print nested lists (each list on a new line) using the print() function.
ex48 = int(input('How many sublists? '))
ex48_nested = []
for s1 in range(ex48):
    ex48_sublist = input(f'Enter items for sublist {s1 + 1} (separated by space): ').split()
    ex48_nested.append(ex48_sublist)

print('Nested list:')
for ex48_sub in ex48_nested:
    print(ex48_sub)

        # 49. Write a Python program to convert a list to a list of dictionaries.
        # Sample lists: ["Black", "Red", "Maroon", "Yellow"], ["#000000", "#FF0000", "#800000", "#FFFF00"]
        # Expected Output: [{'color_name': 'Black', 'color_code': '#000000'}, {'color_name':
        # 'Red', 'color_code': '#FF0000'}, {'color_name': 'Maroon', 'color_code': '#800000'}, {'color_name': 'Yellow', 'color_code': '#FFFF00'}]
ex49_name = input('Enter color names separated by comma: ').split()
ex49_code = input('Enter color codes separated by comma: ').split()

ex49_result = []
for t1 in range(len(ex49_name)):
    ex49_result.append({
        "Color name": ex49_name[t1].strip(),
        "Color code": ex49_code[t1].strip()
    })
print('List of dictionaries:')
print(ex49_result)

        # 50. Write a Python program to sort a list of nested dictionaries.
ex50 = int(input('How many dictionaries? '))

ex50_list = []
for u1 in range(ex50):
    ex50_name = input(f'Enter name for item {u1 + 1}: ')
    ex50_age = int(input(f'Enter age for item {u1 + 1}: '))
    ex50_object = {"Name": ex50_name, "Age": ex50_age}
    ex50_list.append(ex50_object)

print('\nOriginal list of dictionaries:')
for u1 in ex50_list:
    print(u1)

ex50_sort = input('\nEnter the key to sort by (name/age): ').strip().lower()

if ex50_sort in ["Name", "Age"]:
    ex50_sorted_list = sorted(ex50_list, key=lambda v1: v1[ex50_sort])
    print(f'\nSorted list of dictionaries (by {ex50_sort}):')
    for u1 in ex50_sorted_list:
        print(u1)
else:
    print('Invalid choice!')
