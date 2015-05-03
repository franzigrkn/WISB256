document = open('words.txt', 'w')
print (document)
line1= 'Hello \n'
document.write(line1)
line2= 'world \n'
document.write(line2)
line3='goodbye'
document.write(line3)
document.close()

import time
T1 = time.perf_counter()

fin = open('words.txt')

t=[]
for line in fin:
    t=t+[line[0]]
    print(t)

fin.close()
T2 = time.perf_counter()
fin = open('words.txt')

t=[]
for line in fin:
    t.append(line[0])
    print(t)

fin.close()
T3 = time.perf_counter()

print('Time required', T2 - T1, 'sec.')
print('Time required', T3 - T2, 'sec.')

print(int(3.2))














