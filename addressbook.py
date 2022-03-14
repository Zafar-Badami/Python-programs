import pandas as pd
import csv

#name = input("Enter your name: ")
#phone = input("Enter your mobile no.: ")
#print(name, phone)
people = {
    "first_name" : ['Zafar', 'Abid', 'Sajjad', 'Qasim','Abbas'],
    "last_name" : ['Badami', 'Rizvi', 'Devjani', 'Ansari','Sheikh'],
    "phone" : ['90877559','987654300','99887655','78876655','686654449'],
    "email" : ["zafar@email.com","aBid@email.com","saJjad@email.com","wasim@email.com","abbas@email.com"]
    }
people2 = {
    "first_name" : ['Asif', 'Mehmood', 'Basit', 'Bashir','Aslam'],
    "last_name" : ['Qayyum', 'Guznawi', 'Irshad', 'Allawala','Iftikhar'],
    "phone" : ['10877559','687654300','59887655','38876655','986654449'],
    
    }
df = pd.DataFrame(people)
print(df)
df2 = pd.DataFrame(people2)
df=df.append(df2,ignore_index=True,sort=False)
print(df)
#df.to_csv(r'C:\Users\erumz\OneDrive\Desktop\github\Python - Labs\temp.csv')
#df['full_name'] = df['first_name']+' '+df['last_name']
#print(df)
#print(df.drop(columns=['first_name','last_name']))
#print(df['full_name'].str.split(' ',expand=True))
#df[['first_name','last_name']]=df['full_name'].str.split(' ',expand=True)
#print(df)
#df.set_index('email',inplace=True)
#print(df)
#filt = df['email'] == 'abbas@email.com'
#print(df[filt])
#print(df['email'].apply(len))

#def update_email(email):
#    return email.upper()
#print(df['email'].apply(update_email))
#print(df.applymap(str.lower))
#print(df['email'].apply(lambda x:x.lower()))
#print(df.apply(pd.Series.min))
#df['email']=df['email'].str.lower()
#print(df)
#print filt
#print(df.columns)
#print(df.iloc[[0]])
#print(df.iloc[[1,3],2])
#print(df.loc[0:2,"name":"email"])
#print(df.set_index('email'))
