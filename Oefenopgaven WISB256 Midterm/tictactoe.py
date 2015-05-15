rij_1=str(input())
rij_2=str(input())
rij_3=str(input())

invoer=[rij_1, rij_2, rij_3]
for i in range(0,3):
    if (invoer[i])[0]==(invoer[i])[1] and (invoer[i])[1]==(invoer[i])[2]:
        #print('horizontal')
        #print((invoer[i])[0])
        if ((invoer[i])[0])=='1':
            print('Player 1 wins')
        elif (invoer[i])[0]=='2':
            print('Player 2 wins')
      
    elif rij_1[i]==rij_2[i] and rij_2[i]==rij_3[i]:
        #print('vertikal')
        if rij_1[i-1]=='1':
            print('Player 1 wins')
        if rij_1[i-1]=='2':
            print('Player 2 wins')
        
if rij_1[0]==rij_2[1] and rij_2[1]==rij_3[2]:
    #print('diagonaal')
    if rij_1[0]=='1':
        print('Player 1 wins')
    if rij_1[0]=='2':
        print('Player 2 wins')
    else:
        print('No winner')
else:
    print('No winner')
    
