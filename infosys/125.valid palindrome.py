def isPalindrome(s):
       result = "".join(c for c in s if c.isalnum())
       new = ""
       for i in range(len(result)-1,-1,-1):
            new += result[i]
       print(result)
       print(new)     
       return result.lower() == new.lower()
print(isPalindrome("A man, a plan, a canal: Panama"))