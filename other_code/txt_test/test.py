#unknown,M10907324,Trump,Hillary
bbb=[]
ccc=''
f = open('file_io.txt','r')
k = f.readlines()
f.close()
a=k[0].split(',')

for i in range(len(a)):
    bbb.append(a[i])



f = open('file_io.txt', 'w')
bbb.append('M10907322')

for i in range(len(bbb)):
    if i == len(bbb)-1:ccc=ccc+bbb[i]+'\n'
    else:ccc=ccc+bbb[i]+','
print(ccc)
f.write(ccc)
f.close()    