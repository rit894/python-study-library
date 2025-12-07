'''with open ('FH.txt','r+') as f:
    data = f.read()
    print(data)


'''
'''with open("FH.txt",'r') as f:
    for line in f:
        print(line.strip())
with open ('FH.txt','r') as f:
    print(f.read(12).strip())'''
lines = ['python\n','file handling\n', 'prcticals\n']
'''with open ('FH.txt','w') as f:
    f.write('Hello world\n')'''
'''with open('FH.txt', 'r') as f:
    lines = f.readlines()

with open('FH.txt', 'w') as f:
    for line in lines:
        f.write(line)
        if line.strip() == 'prcticals':
            f.write('found you\n')'''
'''with open('FH.txt','a+') as f:
    f.seek(0)
    lines=f.readlines()
    cleanlines=[line.strip() for line in lines]
    print(cleanlines)'''


