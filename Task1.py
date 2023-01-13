from random import choice #imporing choice from random moudule to use later on in the program

#definining 3 lists of values that can be used in the password
constants = ["hello", "house", "what", "love", "glass", "sure", "posh"]
constants1 = ["blue", "green", "yellow", "while", "brown", "red", "grey", "pink"]
constants2 = ["pizza", "burger", "chicken", "coke", "sekuwa", "chips", "cheese", "tomato", "apple"]

#defining a list containing the list names
f = [constants,constants1,constants2]

print("Password Generator")
print("==========================")

while True:
    try:
        number = int(input("\nHow many passwords are needed?: ")) #taking in the number of passwords required

        if 1 <= number <= 24: #checking if the input value between 1 and 24
            for i in range (0, number): #printing as many passwords as required, as long as they're between 1 and 24
                comb = choice(choice(f)) + choice(choice(f)) + choice(choice(f))
                print(i+1,"-->",comb)
            break
        else:
            print("Please input a number between 1 and 24!") #handling the error if the user doesn't input required value

    except ValueError: #checking for ValueError, if a value other than numeric value is entered
        print("Please input valid value!")