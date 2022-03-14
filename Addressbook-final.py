#from asyncio.windows_events import NULL
#from logging import exception
# from turtle import position
# import numpy
import pandas as pd
import os

choice1=0
df = pd.read_csv(r"C:\Users\erumz\OneDrive\Desktop\github\Python - Labs\temp.csv")#index_col='phone')

def main_menu():
    os.system('cls')
    print()
    print()
    print('          BADAMI Address Book')
    print('_____________MENU OPTIONS______________')
    print('|                                      |')
    print('|  1.Add record to AddressBook         |')
    print('|                                      |')
    print('|  2.Delete a record from AddressBook  |')
    print('|                                      |')
    print('|  3.Edit a record from AddressBook    |')
    print('|                                      |')
    print('|  4.Display all data of AddressBook   |')
    print('|                                      |')
    print('|  5.Exit from AddressBook             |')
    print('|                                      |')
    choice = int(input('|_________Enter your selection:________'))
    os.system('cls')
    return(choice)

while choice1!=5:
    try:
        choice1=main_menu()

    except ValueError:
        print("\n Wrong seletion, select between 1-5....") 
        os.system('pause')

    if choice1 == 1:
        name1=input("Enter Frist Name to add record: ")
        # csv_name=df[df['first_name'] == name1]['first_name']
        csv_name=df[df['first_name'] == name1]
        if len(csv_name) != 0:
            print("\nRecord already exits...\n")
            os.system("pause")
        else:
            first_name_add=name1
            last_name_add=input("Enter last name: ")
            phone_add=input("Enter phone number: ")
            email_add=input("Enter email address: ")
            df2={'first_name':first_name_add,'last_name':last_name_add,'phone':phone_add,'email':email_add}
            df=df.append(df2,ignore_index=True)
            print('\nRecord added....\n')
            os.system('pause')

    elif choice1== 2:
        print(df)
        name2=input('Enter First Name to delete the record :')
        filt2 = df['first_name'] == name2
        df=df.drop(index=df[filt2].index)
        print(df)
        os.system('pause')

    elif choice1 == 3:
        name3=input('Enter First Name to Edit the record:')
        filt3 = df['first_name'] == name3
        # csv_name3=df[df['first_name'] == name3]['first_name']
        csv_name3=df[df['first_name'] == name3]
               
        if len(csv_name3)!=0:
            print(df[filt3])
            first_name_add=name3
            last_name_add=input("Enter last name: ")
            phone_add=input("Enter phone number: ")
            email_add=input("Enter email address: ")
            position=df[df['first_name'] == name3].index.values
            df.loc[position,['first_name','last_name','phone','email']] = [first_name_add,last_name_add,phone_add,email_add]
            print('\n Record updated... \n')
            os.system('pause')

        else:
            option=input('Record not found...Do you want to add this (y/n)? ').lower()           
            if option == 'y':
                choice1=1
                continue
            else:
                choice1=3
    elif choice1 == 4:
        print(df)
        os.system('pause')
else:
    df.to_csv(r"C:\Users\erumz\OneDrive\Desktop\github\Python - Labs\temp.csv",index=False)
    exit