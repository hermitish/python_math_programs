# armstrong.py

# examples:- 153, 371

def is_armstrong(n):
    t = n    
    s = 0
    while n:        
        s += (n%10) ** 3        
        n //= 10
    if s == t:
        return True
    else:
        return False
    
print(is_armstrong(153))
