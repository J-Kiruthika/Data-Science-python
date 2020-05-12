## 1. Reading our MoMA Data Set ##

from csv import reader

# Read the `artworks_clean.csv` file
opened_file = open('artworks_clean.csv')
read_file = reader(opened_file)
moma = list(read_file)
moma = moma[1:]

# Convert the birthdate values
for row in moma:
    birth_date = row[3]
    if birth_date != "":
        birth_date = int(birth_date)
    row[3] = birth_date
    
# Convert the death date values
for row in moma:
    death_date = row[4]
    if death_date != "":
        death_date = int(death_date)
    row[4] = death_date

# Write your code below
for i in moma:
    date=i[6]
    if(date!=""):
        i[6]=int(date)
        

## 2. Calculating Artist Ages ##

ages=[]
for i in moma:
    date=i[6]
    birth=i[3]
    if(type(birth)==int):
        ages.append(date-birth)
    else:
        ages.append(0)
final_ages=[]
for i in ages:
    if(i>20):
        final_age=i
    else:
        final_age="Unknown"
    final_ages.append(final_age)

## 3. Converting Ages to Decades ##

# The ages variable is available
# from the previous screen
decades=[]
for i in ages:
    if(i=="Unknown"):
        decades.append(i)
    elif(i!=" "):
        decade=str(i)
        decade=decade[:-1]
        decade=decade+"0s"
        decades.append(decade) 

## 4. Summarizing the Decade Data ##

# The decades variable is available
# from the previous screen
decade_frequency={}
for i in decades:
    if(i not in decade_frequency):
        decade_frequency[i]=1
    else:
        decade_frequency[i]+=1

## 5. Inserting Variables Into Strings ##

artist = "Pablo Picasso"
birth_year = 1881
result="{}'s birth year is{}".format(artist,birth_year)
print(result)

## 6. Creating an Artist Frequency Table ##

artist_freq={}
for i in moma:
    artist=i[1]
    if(artist not in artist_freq):
        artist_freq[artist]=1
    else:
        artist_freq[artist]+=1

## 7. Creating an Artist Summary Function ##

def artist_summary(name):
    
        var=artist_freq[name]
        result="There are {} artworks by {} in the data set".format(var,name)
        print(result)
artist_summary("Henri Matisse")        

## 8. Formatting Numbers Inside Strings ##

pop_millions = [
    ["China", 1379.302771],
    ["India", 1281.935991],
    ["USA",  326.625791],
    ["Indonesia",  260.580739],
    ["Brazil",  207.353391],
]
print("The population of {0} is {1:,.2f}".format("India",1324000000))
for i in pop_millions:
    var1,var2=i[0],i[1]
    print("The population of {0} is {1:,.2f} million".format(var1,var2))

## 9. Challenge: Summarizing Artwork Gender Data ##

momo=open('artworks_clean.csv')
read=reader(momo)
gender=list(read)
gender_freq={}
for i in gender[1:]:
   if(i[5] not in gender_freq):
      gender_freq[i[5]]=1
   else:
      gender_freq[i[5]]+=1
for key,value in gender_freq.items():
    print("There are {0:,} artworks by {1} artists".format(value,key))
        
        
  
 