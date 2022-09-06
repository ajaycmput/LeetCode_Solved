def isPalindrome(s):
    
    # remove all white spaces
    
    s = s.replace(" ","")
    
    # convert all upper case to lower case
    
    s = s.lower()
    
    # remove all non-alphanum characters
    s = ''.join(ch for ch in s if ch.isalnum())
    
    # two pointer method to check palindrome
    lr = 0
    rp = len(s)-1
    
    while ( lr < rp ):
        if s[lr] != s[rp]:
            return False
        
        lr += 1
        rp -= 1
        
    return True