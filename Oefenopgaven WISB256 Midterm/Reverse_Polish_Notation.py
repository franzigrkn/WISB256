RPN = input()
print(RPN)
uitspraak=RPN

index_1=uitspraak.find(' ')
#print(index_1)

index_2=uitspraak.find(' ', int(index_1)+1)
#print(index_2)

deel_1=uitspraak[:int(index_1)]
deel_2=uitspraak[int(index_1)+1:index_2]
deel_3=uitspraak[int(index_2):]
#print(deel_1)
#print(deel_2)
#print(deel_3)
result= int(deel_1) + (deel_3) + int(deel_2)
print(result)



