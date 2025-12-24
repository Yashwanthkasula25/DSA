# name = "yashwanth"
# #name = name.replace('a', "")
# new = ""
# dup = str(input("enter element"))
# for i in name:
#     if dup!=i:
#         new += i
        
# print(new)        


# name = 'yashwanth'
# new = ''
# for i in name:
#     if i not in new:
#         new += i
# print(new)        



# name = "John"
# age = 25
# print(f"My name is {name}, age is {age}")
# print("Name: {}, Age: {}".format(name, age))

# name = 'yash'
# new = name[::-1]
# print(new)


# name = 'appa'
# new = name[::-1]
# if name == new:
#     print("palindrome")
# else:
#     print("not palindrome")    


# name = 'watermelon'
# vowels = "aeiouAEIOU"
# vow = 0
# con = 0
# new_vow = ""
# new_con = ""
# for i in name:
#     if i in vowels:
#         vow += 1
#         new_vow += i
#     else:
#         con += 1    
#         new_con += i
# print(f"no of vowels is {vow} and they are {new_vow}")
# print(f"no of consonants {con} and they are {new_con}")

# name = 'Yashwanth'
# dict = {}
# for i in name:
#     if i in dict:
#         dict[i] += 1
#     else:
#         dict[i]=1
# for a,b in dict.items():
#     print(f"{a} : {b}")


# name = ' yash  '
# print(name.strip())

# name1  = "yash"
# name2 = 'kasula'
# name3 = 'goud'



# # print(name1[0].upper() + name1[1:]) 
# # print(name2[0].upper() + name2[1:])
# # print(name3[0].upper() + name3[1:])
# print(name1.title() , name2.title() ,name3.title())  



# def underscore():
#     sentence = str(input('enter string'))
#     remove = sentence.replace(' ','_')
#     return remove
# print(underscore())    

    

# a = str(input("enter string "))
# b = str(input("enter string "))
# c = ''.join(sorted(a))
# d = ''.join(sorted(b))
# if c == d:
#     print('they are anagram')
# else:
#     print('not anagram')    



# name = "yash"
# print(name.upper())
# print(name.lower())
# print(name.title())

# import string
# name = " hi! hello, namstey??"
# new = ''
# for i in name:
#     if i not in string.punctuation:
#         new += i
# print(new) 


# import string
# def longest():
#     name = str(input("enter a sentence "))
#     clean = ""
#     for i in name:
#         if i not in string.punctuation:
#             clean += i
#     splitted = clean.split()
#     long = max(splitted,key=len)
#     return long
# print(longest)    




# name = 'yash'
# unique = ''
# for i in name:
#     if i in unique:
#         print(f"{i} is not unique")
#         break
#     else:
#         #print(f"{i} is unique")
#         unique += i
# if len(name) == len(unique):
#     print(f"{name} is unique")



# name = 'kasula'
# count = {}
# for i in name:
#      count[i] = count.get(i, 0) + 1
# for i in name:
#     if count[i] == 1:
#         print(f"First non repeating character is: {i}")
#         break
# else:
#     print("No non repeating character found.")



# name = 'yashwanth'
# b = 3
# print(str(b) + name)

# name = "sai raammm sai rammmmmm"
# new = '_'.join(name.lower().split())  
# print(new)



# def to_camel_case(sentence):
#     words = sentence.lower().split()
#     return words[0] + ''.join(word.capitalize() for word in words[1:])

# # Example
# s = "sai raaaaaammmmmmmmmmmm sai raaaaaammmmm"
# print(to_camel_case(s))



# name = 'yashwanth'
# print(''.join(sorted(name)))



# name = 'yela hela hela heyyyyyyyyy'
# splitt = name.split()
# reverse = splitt[::-1]
# new = ' '.join(reverse)
# print(new)



# name = 'yela hela hela heyyyyyyyyy'
# print(name.count('he'))



n = int(input("enetr length of list"))
list = []
for _ in range(n):
    list = input("enter elements ").split()
print(list)




