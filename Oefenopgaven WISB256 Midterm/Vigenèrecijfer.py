word = input()
code = input()
lengte_word= len(word)
lengte_code = len(code)
#print(type(word))
#print(lengte_word)
#print(lengte_code)
for i in range(0, int(lengte_word)):
    orde_word_i=ord(word[i])%97
    #print(orde_word_i)
for i in range(0, int(lengte_code)):
    orde_code_i=ord(code[i])%97
    #print(orde_code_i)
result=''
for i in range(0, int(lengte_word)):
    y=i%(lengte_code)
    x= 26 - (ord(code[y])%97)
    #print(y)
    #print(x)
    z= (ord(word[i])%97 + x)%26
    #print(z)
    result = result + chr(z+97)
    #print(result)
print(result)
    
    
    