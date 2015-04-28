document = open('words.txt', 'w')
print (document)
line1= 'Hello \n'
document.write(line1)
line2= 'world \n'
document.write(line2)
line3='goodbye'
document.write(line3)
document.close()

fin = open('words.txt')

t=[]
for line in fin:
    t=t+[line[0]]
    print(t)

fin.close()







