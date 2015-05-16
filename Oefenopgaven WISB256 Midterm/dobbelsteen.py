number=int(input())
unten=1
links=2
rechts=5
vorne=4
hinten=3
oben=6

dobbelsteen=[6,5,1,2,3,4]

for i in range(1,number+1):
    input_i=input()
    if input_i in ['omhoog']:
        dobbelsteen=[dobbelsteen[5], dobbelsteen[1],dobbelsteen[4], dobbelsteen[3], dobbelsteen[0], dobbelsteen[2]]
        #print(dobbelsteen)
    if input_i in ['omlaag']:
        dobbelsteen=[dobbelsteen[4], dobbelsteen[1],dobbelsteen[5], dobbelsteen[3], dobbelsteen[2], dobbelsteen[0]]
        #print(dobbelsteen)
    if input_i in ['rechts']:
        dobbelsteen=[dobbelsteen[3], dobbelsteen[0],dobbelsteen[1], dobbelsteen[2], dobbelsteen[4], dobbelsteen[5]]
        #print(dobbelsteen)
    if input_i in ['links']:
        dobbelsteen=[dobbelsteen[1], dobbelsteen[2],dobbelsteen[3], dobbelsteen[0], dobbelsteen[4], dobbelsteen[5]]
        #print(dobbelsteen)

#print(dobbelsteen)
answer=dobbelsteen[0]
print(answer)






    