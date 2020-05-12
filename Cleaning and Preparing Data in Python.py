## 1. Introducing Data Cleaning ##

num_rows=len(moma)
print(num_rows)


## 2. Reading our MoMA Data Set ##

opened_file=open("artworks.csv")
read_file=reader(opened_file)
moma=list(read_file)
moma=moma[1:]



## 3. Replacing Substrings with the replace Method ##

age1 = "I am thirty-one years old"
age2 = age1.replace("one","two")
print(age2)

## 4. Cleaning the Nationality and Gender Columns ##

for row in moma:
    nationality=row[2]
    gender=row[5]
    nationality=nationality.replace("(","")
    gender=gender.replace("(","")
    nationality=nationality.replace(")","")
    gender=gender.replace(")","")
    row[2]=nationality
    row[5]=gender
    
    

## 5. String Capitalization ##

for row in moma:
    Gender=row[5]
    Nationality=row[2]
    Gender=Gender.title()
    Nationality=Nationality.title()
    if not Gender:
        Gender="Gender Unknown/Other"
    row[5]=Gender    
    if not Nationality:
        Nationality="Nationality Unknown"
    row[2]=Nationality    
    
    

## 6. Errors During Data Cleaning ##

def clean_and_convert(date):
    if(date!=""):
        date=date.replace("(","")
        date=date.replace(")","")
        date=int(date)
    return date
for row in moma:
    BeginDate=row[3]
    EndDate=row[4]
    BeginDate=clean_and_convert(BeginDate)
    EndDate=clean_and_convert(EndDate)
    row[3]=BeginDate
    row[4]=EndDate
    


      
    

## 7. Parsing Numbers from Complex Strings, Part One ##

test_data = ["1912", "1929", "1913-1923",
             "(1951)", "1994", "1934",
             "c. 1915", "1995", "c. 1912",
             "(1988)", "2002", "1957-1959",
             "c. 1955.", "c. 1970's", 
             "C. 1990-1999"]

bad_chars = ["(",")","c","C",".","s","'", " "]
def strip_characters(string):
    for i in bad_chars:
        string=string.replace(i,"")
    return string
stripped_test_data=[]
for i in test_data:
    stripped_test_data.append(strip_characters(i))
    

## 8. Parsing Numbers from Complex Strings, Part Two ##

test_data = ["1912", "1929", "1913-1923",
             "(1951)", "1994", "1934",
             "c. 1915", "1995", "c. 1912",
             "(1988)", "2002", "1957-1959",
             "c. 1955.", "c. 1970's", 
             "C. 1990-1999"]

bad_chars = ["(",")","c","C",".","s","'", " "]

stripped_test_data = ['1912', '1929', '1913-1923',
                      '1951', '1994', '1934',
                      '1915', '1995', '1912',
                      '1988', '2002', '1957-1959',
                      '1955', '1970', '1990-1999']
def bad_char(string):
    for i in bad_chars:
        string.replace(i," ")
    return string
def process_date(string):
    if "-" in string:
        list=string.split("-")
        sum=int(list[0])+int(list[1])
        date=round(sum/2)
    else:
        date = int(string)
    return date

processed_test_data = []


for row in moma:
    date = row[6]
    first = strip_characters(date)
    second = process_date(first)
    row[6] = second
for d in stripped_test_data:
    date = process_date(d)
    processed_test_data.append(date)
