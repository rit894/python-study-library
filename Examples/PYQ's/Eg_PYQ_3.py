'''agriculture={
    'millet':{
        'type': 'cereal',
        'top 3 producers': ['India', 'Nigeria', 'china']},

    'green pea':{
        'type': 'vegetable',
        'top 3 producers': ['India', 'China', 'pakistan']},

    'papaya':{
        'type': 'fruit',
        'top 3 producers': ['India', 'Indonesia', 'brazil']},

    'almond':{
        'type': 'nut',  
        'top 3 producers': ['USA', 'spain', 'iran']}


}
def max_producer():
  dict1={}
  for product, producer in agriculture.items():
    for  countries  in producer['top 3 producers']: 
      dict1[countries]=dict1.get(countries,0)+1
  for country,count in dict1.items():
      if count==max(dict1.values()):
         print(country,'is the top producer country')'''

'''n=int(input())

for i in range(n):
   product=input()
   tpye_of_product=input()
   top_3producers=input().split(',')
   agriculture+i=Agriculture(product,tpye_of_product,top_3producers)
   '''

'''class Agriculture:
   def __init__(self,product,type_of_product,top_3producers):
       self.product=product
       self.type_of_product=type_of_product
       self.top_3producers=top_3producers
   def max_producer(self):
         dict1={}
        for 
n=int(input())
list1=[]
for i in range(n):
   product=input()
   tpye_of_product=input()
   top_3producers=input().split(',')
   agriculture+i=Agriculture(product,tpye_of_product,top_3producers)
   for j in range(1):
        list1.append(tuple(agriculture+i))
    '''
'''FAOSTAT, the Food Agriculture Organization of the United Nations, keeps track of the 
production of different types of Crops worldwide. It stores the following details – Name of the 
crop, Type (Cereal, Vegetable, Fruit, and Nuts), and the top three largest producers (country 
names). The organization has approached you to do some analysis of their data. Unluckily, they 
do not have a soft copy of their data. You need to enter the details for N crops and find answers 
to the following two questions:  
 Which country tops the table for the maximum number of crops?  
 Given a country name, for how many crops, it appears in the top three?  
Design and implement a nested list-based Python solution to read the details of N countries and 
answer the above questions. [10 marks] [CO2] [BTL3]  
Input Format  
The first input is the number of crops, N. The next 3*N inputs are the Name of the country, 
Type, and List of top three country names (all inputs are strings) for each crop. The last input 
is the country name for the second question, “For how many crops, the given country’s name 
appear in the top three?”  
Output Format 
The program prints the country's name that appears in the top three for the maximum number 
of crops. If multiple countries satisfy the above condition, you need to print only the first 
country's name. The second line prints the count of crops for which the country's name appears 
in the top three tables. 
N=int(input())'''
Agriculture={}
N=int(input())
for i in range(N):
    product=input()
    type_of_product=input()
    top_3producers=input().split()
    Agriculture[product]={
        'type': type_of_product,
        'top 3 producers': top_3producers
    }
def max_producer():
  dict1={}
  for product, producer in Agriculture.items():
    for  countries  in producer['top 3 producers']: 
      dict1[countries]=dict1.get(countries,0)+1
  for country,count in dict1.items():
      if count==max(dict1.values()):
         print(country,'is the top producer country')
max_producer()
def max_number():
    country_name=input()
    count=0
    for product , producers in Agriculture.items():
        if country_name in producers['top 3 producers']:
            count+=1
    print(count)
max_number()
    
   

    
    