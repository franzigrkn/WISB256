
def sum_of_squares(n):
    x=0
    for i in range(1,n+1):
        x=x+i**2
    return x
    
def square_of_sum(n):
    y=0
    for i in range(1,n+1):
        y=y+i
    z=y**2
    return z

answer= abs(sum_of_squares(100) - square_of_sum(100))
print(answer)
    
