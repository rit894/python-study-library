dict1 = {}

with open("FH_2.txt", 'r') as f:
    for line in f:
        parts = line.strip().split(',')


        sport_name = parts[0]
        participant_form = parts[1]
        countries1 = parts[2].strip("[]")
        countries2=parts[3]
        countries3=parts[4].strip(']')
        olympic_status = parts[5]
        list1=[countries1,countries2,countries3]

        dict1[sport_name] = {
            'Category': participant_form,
            'Top countries': list1,
            'Olympic Status': olympic_status
        }

print(dict1)
print(list(dict1))
country= input().title()
dict2={}
for sport, details in dict1.items():
   if country in details['Top countries']:
       if country not in dict2:
        dict2[country]=[]
       dict2[country].append(sport)
print(dict2)
dict3={}
for sport , details in dict1.items():
   if details['Category']=='Team':
      dict3['Team']=dict3.get('Team',0)+1
   elif details['Category']=='Individual':
      dict3['Individual']=dict3.get('Individual',0)+1
print(dict3)
print(set(dict1))