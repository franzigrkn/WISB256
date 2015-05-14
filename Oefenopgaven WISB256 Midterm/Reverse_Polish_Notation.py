import operator

RPN = input()
#print(RPN)
uitspraak=RPN

index_1=uitspraak.find(' ')
#print(index_1)

index_2=uitspraak.find(' ', int(index_1)+1)
#print(index_2)

deel_1=uitspraak[:int(index_1)]
deel_2=uitspraak[int(index_1)+1:index_2]
deel_3=uitspraak[int(index_2)+1:]
#print(deel_1)
#print(deel_2)
#print(deel_3)

#print(type(deel_3))
result_string = deel_1 + deel_3 + deel_2
result=eval(result_string)
#print(result)

result_3="{0:.3f}".format(result)
print(result_3)



