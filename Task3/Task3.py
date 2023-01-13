#importing all the necessary modules
import sys
import re
import random

def stu_email(filename):
    '''A function to take an input of a file name and create unique email addresses from the data given in the file'''
    
    #opening the file and creating a list with the lines in the file
    with open(filename, 'r') as file1:
        list1 = file1.readlines()

    #creating separate lists for names, ids and emails
    ids = [i[:8] for i in list1]
    names = [j[9:] for j in list1]
    mails = []

    for j in names:
        names1 = j.split(", ") #separating the last and forenames
         
        last = re.sub(r'[^a-zA-Z]', '', names1[0].lower()) #removing all unrequired special characters
        first_initials = [i[0].lower() for i in names1[1].split(" ")] #making a list with just the first name initials
        initial_join = '.'.join(first_initials) #joining the initials with a dot, as specified
        
        email = initial_join + "." + last + str(random.randint(1000,9999)) + "@poppleton.ac.uk" #creating a unique email for each student
        mails.append(email) #adding the email to the mails list
        
    with open('email_addresses.txt', 'w') as file2: #opening the output file
        for a in range(0,len(mails)): #writing the ids and emails in the output file
            file2.write(f"{ids[a]} {mails[a]} \n")
    
try:
    stu_email(sys.argv[1]) #calling the function with the parameter user input in the terminal
    
except IndexError: #printing an error when user doesn't input any file name
    print("Error: Missing command-line argument.")
    
except FileNotFoundError: #printing an error when the file name doesn't exist
    print(f"Error: Cannot open \"{sys.argv[1]}\". Sorry about that.")