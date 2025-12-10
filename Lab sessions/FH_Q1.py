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
n=int(input())
for i in range(n):
        choosing=int(input())
        if choosing==1:
            with open('FH.txt','r') as f:
                print(f.read())
        elif choosing == 2:
            author = input("Enter author name: ").strip()
            with open("FH.txt", 'r') as f:
                for line in f:
                    if author.lower() in line.lower():
                        parts=line.strip().split(',')
                        book_name=parts[1]
                        print(book_name)
        elif choosing==3:
            dict1={}
            with open ('FH.txt','r') as f:
                for line in f:
                    parts=line.strip().split(',')
                    book_name=parts[1]
                    cost=parts[3]
                    dict1[book_name]=int(cost)
                maxValue=max(dict1.values())
                for key , value in dict1.items():
                    if int(value)==maxValue :
                        print(key, value)
        elif choosing == 4:
            set1=set()
            with open ('FH.txt','r') as f:
                for line in f:
                    parts= line.strip().split(',')
                    genere=parts[4]
                    set1.add(genere)
            print(set1)
        elif choosing == 5:
            with open ('FH.txt','a+') as f:
                book_code=input()
                book_name=input()
                authour=input()
                cost=input()
                genere=input()
                f.write(f"{book_code},{book_name},{authour},{cost},{genere}\n")
        elif choosing == 6:
            print('Thank you  for using services...')
            






