#importing the necessary modules
import sys
import string
from statistics import mode

#making lists with all the letters in the English alphabet, both capital and small
lowercase = list(string.ascii_lowercase) 
uppercase = list(string.ascii_uppercase)
letters = ['e', 't', 'a', 'i', 'o', 'n', 's', 'h', 'r'] #a list of the most common letters in the English alphabet

def decryption(filename):
    '''Takes in a file containing a code possibly decoded with caesar code and deciphers the code accordingly'''
    
    with open(filename,"r") as file, open("common_words.txt", "r") as file1: #opening the file containing the decrypted code and 100 most common words in the English alphabet
        to_decrypt = list(file.read()) #creating a list with every character in the decrypted text
        words = file1.read().split("\n") #creating a list with the 100 most common words in the English alphabet
    check = 0
    
    for i in range(1,25): #checking the code with each and every letter of the alphabet as its key
        
        decoded = "" #creating an empty string to store the decoded code
        
        #making encrypted lists for both uppercase and lowercase letters
        encrypted_lowercase = lowercase[i:] + lowercase[:i]
        encrypted_uppercase = uppercase[i:] + uppercase[:i]
 
        for j in to_decrypt: #checking and individually decoding each character in the code
            if j in lowercase:
                decoded += encrypted_lowercase[lowercase.index(j)]
            elif j in uppercase:
                decoded += encrypted_uppercase[uppercase.index(j)]
            else:
                decoded += j

        count = 0
        decoded_final = list(decoded.replace(" ", "")) #creating a list with all the DECODED characters
        
        if mode(decoded_final) in letters: #checking to see if the letter with the highest frequency is among the most common ones in the English alphabet
            for x in decoded.split(" "): 
                if x in words: #checking if the most common words in the English alphabet are in our decoded list
                    count += 1
            if count > 3:
                print(decoded)
                check += 1 #updating the flag value we introduced earlier
    
    if check == 0: #printing an error if the code wasn't deciphered with caeser code
        print("Cannot decrypt. Most likely not a Caesar Cypher at work here.")
        
try:
    decryption(sys.argv[1])

except FileNotFoundError: #printing an error when the file is not found
    print(f"Cannot open \"{sys.argv[1]}\". Sorry about that.")

except IndexError: #printing an error when no file name is input
    print("Sorry. Didn't catch the file name!")