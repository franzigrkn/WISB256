invoer= input()

if 'g' not in invoer and int(invoer)==1:
    print('Ug!')
if 'g' not in invoer and int(invoer) >1:
    print('Ug '+'ug '*(int(invoer) -2) + 'ug!')
if 'g' in invoer:
    count=0
    for letter in invoer:
        if letter == ' ':
            count=count+1
    print(count +1)