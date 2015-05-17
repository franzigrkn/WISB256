fibonacci_getallen=[1,2]



def fibonacci(number):
    for i in range(0, number):
        new=fibonacci_getallen[i]+fibonacci_getallen[i+1]
        if new < 4000000:
            fibonacci_getallen.append(new)
        else:
            return(fibonacci_getallen)
            
            
def even_fibonacci(lijst):
    n=len(lijst)
    even=[]
    #print(n)
    for i in range(0,n):
        if lijst[i]%2 == 0:
            even.append(lijst[i])
    return(even)
    
invoer=int(input())
fibonacci_getallen_2=fibonacci(invoer)
print(fibonacci_getallen_2)

    
answer_list=even_fibonacci(fibonacci_getallen_2)
print(answer_list)

answer=sum(answer_list)
print(answer)







    

    
    
    