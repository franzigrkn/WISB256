number=input()
#print(number)
getallen= list(range(1, int(number)+1))
#print(getallen)
for i in range(1, int(number)+1):
    uitspraak_i = input()
    count=0
    for letter in uitspraak_i:
        if letter == ' ':
            count=count+1
    #print(count+1)
    if count +1 > 4:
        print('Crackers!')
    else:
        print(uitspraak_i + ' krAh!')