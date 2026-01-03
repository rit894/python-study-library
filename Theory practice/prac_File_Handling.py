

#  Alternative way to read a file
'''with open('demofile.txt', 'r') as f:
     print(f.read())'''
#read file without using with statement
#r"D:\2024\Diwali 2024\IMG.jpg"
'''f=open('D:\\mydrive\\python\\Theory practice\\demofile.txt','r')
print(f.read())
f.close()'''
# read only one line of the file 
'''with open("demofile.txt") as f:
  print(f.readline())'''
#loop through the file line by line
'''with open("demofile.txt") as f:
  for x in f:
    print(x)'''
# Write Write to an existing file
#append methode
'''with open('demofile.txt','a') as f:
    f.write('this file now has more content!')
with open('demofile.txt') as f:
    print(f.read())'''
# wrtie methode
'''with open("demofile.txt", "w") as f:
  f.write("Woops! I have deleted the content!")
with open("demofile.txt") as f:
  print(f.read())'''
#Create a New File
'''"x" - Create - will create a file, returns an error if the file exists

"a" - Append - will create a file if the specified file does not exists

"w" - Write - will create a file if the specified file does not exists

f = open("myfile.txt", "x")'''
# Delete a File
'''import os 
os.remove("demofile.txt")

import os

file_path = r"D:\2024\Diwali 2024\IMG20241101063138.jpg"

if os.path.exists(file_path):
    with open(file_path, "rb") as f:
        data = f.read()
        print("File read successfully. Size:", len(data), "bytes")
else:
    print("File not found. Please check the path or filename.")

'''
#for deleteing an entire file
'''import os
os.rmdir("myfolder")'''
          
with open("FH_2.txt", 'r') as f:
    for line in f:
        if 'chess' in line:
            line.delete()