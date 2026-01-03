songs={
    'smooth_criminal':{
        'Artist':'Michael Jackson',
        'Genre':['R&B'],
        'Year':1987

    },
    'macarena':{
        'Artist':'Los Del Rio',
        'Genre':['pop'],
        'Year':1993
    },

    'The rose':{
        'Artist':'LeAnn Rimes',
        'Genre':['Country'],  
        'Year':1997},

    'Dangerous':{
        'Artist':'Michael Jackson',
        'Genre':['R&B','Pop'],
        'Year':1991},
    'They dont_care_about_us':{
        'Artist':'Michael Jackson',
        'Genre':['R&B','Pop'],
        'Year':1995},
    'Set _fire_to_the_rain':{
        'Artist':'Adele',
        'Genre':['Pop'],
        'Year':2011},
    'Hello':{
        'Artist':'Adele',
        'Genre':['soul'],
        'Year':2015},
    'livin la vida loca':{
        'Artist':'Ricky Martin',
        'Genre':['Pop','Rock'],
        'Year':1999},
    'Shape of you':{
        'Artist':'Ed Sheeran',  
        'Genre':['Pop'],
        'Year':2017},
    'Unstoppable':{
        'Artist':'Sia',
        'Genre':['Indie','Pop','EDM'],
        'Year':2016}

}
def Artist(a):
    set1=set()
    for details in a:
        set1.add(details['Artist'])
    return set1

(Artist(songs.values()))

def popular_Genres(a):
    set1=set()
    for details in a:
        set1.update(details['Genre'])
    return set1
print(popular_Genres(songs.values()))

def lovedDecade():
    decade_dict={}
    for name, details in songs.items():
        if 1981<= details['Year']<=1990:
            decade_dict['1981-1990']=decade_dict.get('1981-1990',0)+1
        elif 1991<= details['Year']<=2000:
            decade_dict['1991-2000']=decade_dict.get('1991-2000',0)+1
        elif 2001<= details['Year']<=2010:
            decade_dict['2001-2010']=decade_dict.get('2001-2010',0)+1
        elif 2011<= details['Year']<=2020:
            decade_dict['2011-2020']=decade_dict.get('2011-2020',0)+1
    for decade,count in decade_dict.items():
        if count==max(decade_dict.values()):
            print(decade,'--',count)


lovedDecade()
def genreFrequency(a):
    dict_1={}
    for song,details in songs.items():
        for gen in a:
            if gen in details['Genre']:
                dict_1[gen]=dict_1.get(gen,0)+1
    print(dict_1)
genreFrequency(popular_Genres(songs.values()))

def artistwiseGenre(a, b, c):
    dict_1 = {}
    for details in a:
        artist = details['Artist']
        if artist not in dict_1:
            dict_1[artist] = {genre: 0 for genre in c}  
        for g in details['Genre']:
            if g in c:
                dict_1[artist][g] += 1  
    return dict_1 

print(artistwiseGenre(songs.values(), Artist(songs.values()), popular_Genres(songs.values())))
def my_function(*kids):
  print("The youngest child is " + kids[1])
my_function("Emil", "Tobias", "Linus")


