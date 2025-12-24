# # ✅ 1. Reverse a String

# s = "hello"
# reversed_s = s[::-1]
# print(reversed_s)  # Output: "olleh"


# # ✅ 2. Check if a Number is Prime

# n = 7
# is_prime = True
# if n <= 1:
#     is_prime = False
# for i in range(2, int(n**0.5) + 1):
#     if n % i == 0:
#         is_prime = False
#         break
# print("Prime" if is_prime else "Not Prime")


# # ✅ 3. Fibonacci Series (upto n terms)

# n = 10
# a, b = 0, 1
# for _ in range(n):
#     print(a, end=' ')
#     a, b = b, a + b


# # ✅ 4. Factorial of a Number

# def factorial(n):
#     result = 1
#     for i in range(2, n+1):
#         result *= i
#     return result

# print(factorial(5))  # Output: 120


# # ✅ 5. Palindrome Check (String/Number)

# s = "madam"
# print("Palindrome" if s == s[::-1] else "Not Palindrome")


# # ✅ 6. Find Largest Element in a List

# lst = [2, 9, 1, 7]
# print(max(lst))  # Output: 9




# # ✅ 7. Sum of Digits of a Number


# n = 1234
# digit_sum = sum(int(digit) for digit in str(n))
# print(digit_sum)  # Output: 10



# # ✅ 8. Count Vowels in a String


# s = "Python Programming"
# vowels = "aeiouAEIOU"
# count = sum(1 for char in s if char in vowels)
# print(count)



# # ✅ 9. Swap Two Numbers


# a, b = 5, 10
# a, b = b, a
# print(a, b)  # Output: 10 5



# # ✅ 10. Even or Odd Check


# n = 7
# print("Even" if n % 2 == 0 else "Odd")



# # ✅ 11. Remove Duplicates from List


# lst = [1, 2, 2, 3, 4, 4, 5]
# unique = list(set(lst))
# print(unique)



# # ✅ 12. Check Armstrong Number (e.g. 153 = 1³ + 5³ + 3³)


# n = 153
# sum_cubes = sum(int(d)**3 for d in str(n))
# print("Armstrong" if sum_cubes == n else "Not Armstrong")



# ✅ 13. Print Pattern (Right Triangle)


# n = 5
# for i in range(1, n+1):
#     print("*" * i)
# Output:



# *
# **
# ***
# ****
# *****



# ✅ 14. Count Frequency of Characters in a String


# from collections import Counter
# s = "banana"
# print(Counter(s))  # Output: {'b': 1, 'a': 3, 'n': 2}



# ✅ 15. Check Leap Year


# year = 2024
# is_leap = (year % 4 == 0 and (year % 100 != 0 or year % 400 == 0))
# print("Leap Year" if is_leap else "Not Leap Year")









# ✅ 1. Anagram Check
# Two strings are anagrams if they contain the same characters in the same frequency.



# def is_anagram(str1, str2):
#     return sorted(str1) == sorted(str2)

# print(is_anagram("listen", "silent"))  # True
# print(is_anagram("hello", "world"))    # False



# ✅ 2. Check if a String is a Pangram
# A pangram contains every letter of the alphabet at least once.



# import string

# def is_pangram(s):
#     alphabet = set(string.ascii_lowercase)
#     return alphabet <= set(s.lower())

# print(is_pangram("The quick brown fox jumps over the lazy dog"))  # True



# ✅ 3. Find the First Non-Repeating Character


# from collections import Counter

# def first_non_repeating_char(s):
#     freq = Counter(s)
#     for ch in s:
#         if freq[ch] == 1:
#             return ch
#     return None

# print(first_non_repeating_char("aabbccdef"))  # Output: d



# ✅ 4. Find All Duplicates in a List


# from collections import Counter

# def find_duplicates(lst):
#     freq = Counter(lst)
#     return [item for item, count in freq.items() if count > 1]

# print(find_duplicates([1, 2, 2, 3, 4, 4, 5]))  # Output: [2, 4]



# ✅ 5. Find Missing Number in a Range
# Example: Given [1, 2, 4, 5] → Missing number is 3



# def find_missing(lst, n):
#     return (n * (n + 1)) // 2 - sum(lst)

# print(find_missing([1, 2, 4, 5], 5))  # Output: 3



# ✅ 6. Count Words in a Sentence


# sentence = "Python is easy to learn"
# words = sentence.split()
# print("Word count:", len(words))  # Output: 5



# ✅ 7. Check if List is Sorted


# lst = [1, 2, 3, 4]
# print(lst == sorted(lst))  # True



# ✅ 8. Find All Pairs with Given Sum


# def find_pairs(lst, target):
#     seen = set()
#     pairs = []
#     for num in lst:
#         if target - num in seen:
#             pairs.append((num, target - num))
#         seen.add(num)
#     return pairs

# print(find_pairs([1, 2, 3, 4, 5], 6))  # [(3, 3), (4, 2), (5, 1)]



# ✅ 9. Find Second Largest Number


# lst = [1, 2, 3, 4, 5]
# unique = list(set(lst))
# unique.sort()
# print(unique[-2])  # Output: 4



# ✅ 10. Remove All Punctuation from String


# import string

# text = "Hello, world! Python is awesome :)"
# clean = ''.join(ch for ch in text if ch not in string.punctuation)
# print(clean)




# ✅ Bonus: Interview Tricky String Question
# 🔹 Reverse Words in a Sentence


# s = "I love Python"
# print(' '.join(reversed(s.split())))  # Output: "Python love I"



# ✅ 1. Right-Angled Triangle


# n = 5
# for i in range(1, n + 1):
#     print("*" * i)


# *
# **
# ***
# ****
# *****


# ✅ 2. Inverted Right-Angled Triangle


# n = 5
# for i in range(n, 0, -1):
#     print("*" * i)


# *****
# ****
# ***
# **
# *


# ✅ 3. Right-Aligned Triangle


# n = 5
# for i in range(1, n + 1):
#     print(" " * (n - i) + "*" * i)


#     *
#    **
#   ***
#  ****
# *****


# ✅ 4. Pyramid Pattern


# n = 5
# for i in range(n):
#     print(" " * (n - i - 1) + "*" * (2 * i + 1))
# markdown
# Copy
# Edit
#     *
#    ***
#   *****
#  *******
# *********


# ✅ 5. Diamond Pattern


# n = 5
# for i in range(n):
#     print(" " * (n - i - 1) + "*" * (2 * i + 1))
# for i in range(n - 2, -1, -1):
#     print(" " * (n - i - 1) + "*" * (2 * i + 1))


#     *
#    ***
#   *****
#  *******
# *********
#  *******
#   *****
#    ***
#     *
# 🔢 NUMBER PATTERNS


# ✅ 6. Number Triangle


# n = 5
# for i in range(1, n + 1):
#     for j in range(1, i + 1):
#         print(j, end=" ")
#     print()


# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5


# ✅ 7. Repeated Number Triangle


# n = 5
# for i in range(1, n + 1):
#     print((str(i) + ' ') * i)


# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5


# ✅ 8. Number Pyramid

# n = 5
# for i in range(1, n + 1):
#     print(" " * (n - i), end="")
#     num = 1
#     for j in range(1, 2 * i):
#         print(num, end="")
#         if j < i:
#             num += 1
#         else:
#             num -= 1
#     print()


#     1
#    121
#   12321
#  1234321
# 123454321
# 🔤 CHARACTER PATTERNS


# ✅ 9. Alphabet Triangle


# n = 5
# for i in range(n):
#     ch = 'A'
#     for j in range(i + 1):
#         print(ch, end=' ')
#         ch = chr(ord(ch) + 1)
#     print()


# A
# A B
# A B C
# A B C D
# A B C D E


# ✅ 10. Right-Aligned Alphabet Pattern

# n = 5
# for i in range(n):
#     print(" " * (n - i - 1), end="")
#     for j in range(i + 1):
#         print(chr(65 + j), end="")
#     print()

#     A
#    AB
#   ABC
#  ABCD
# ABCDE
# 🔁 OTHER PATTERNS


# ✅ 11. Floyd’s Triangle

# n = 5
# num = 1
# for i in range(1, n + 1):
#     for j in range(i):
#         print(num, end=' ')
#         num += 1
#     print()

# 1
# 2 3
# 4 5 6
# 7 8 9 10
# 11 12 13 14 15


# ✅ 12. Pascal’s Triangle

# def factorial(n):
#     f = 1
#     for i in range(2, n + 1):
#         f *= i
#     return f

# n = 5
# for i in range(n):
#     for j in range(n - i + 1):
#         print(" ", end="")
#     for j in range(i + 1):
#         print(factorial(i) // (factorial(j) * factorial(i - j)), end=" ")
#     print()


#      1 
#     1 1 
#    1 2 1 
#   1 3 3 1 
#  1 4 6 4 1 




# list
  