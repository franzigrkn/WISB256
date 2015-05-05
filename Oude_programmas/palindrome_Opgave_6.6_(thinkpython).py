def first(word):
    return word[0]
    
def last(word):
    return word[-1]
    
def middle(word):
    return word[1:-1]
    




def is_palindrome(word):
    if len(word)==0:                         #voor het geval dat we een even lengte van word hebben
        return True
    elif len(word)==1:                       #voor het geval dat we een oneven lengte van word hebben
        return True
    elif len(word) > 1:                      #voor alle getallen met lengte groter dan 1
        if first(word)==last(word):
            newword= str(middle(word))
            is_palindrome(newword)
        else: 
            return False
    
        
print(is_palindrome('hh'))

    
        
    

    