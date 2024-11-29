#Palindrome

def is_palindrome(s, first, last):
    # Base case 1
    if first == last:
        return True
    
    elif s == "":
        return True
    
    # Base case 2
    elif s[first] != s[last]:
        return False

    #Recursive case
    return is_palindrome(s, first + 1, last - 1)

def check_palindrome(s):
   
    return is_palindrome(s, 0, len(s) - 1)

# Test cases
print(check_palindrome("tacocat"))  