print("Park Run Timer \n~~~~~~~~~~~~~~ \nLet's go!\n")

data = {} #creating a dictionary to hold the data

while True:
    ans = input()
    new = ans.split("::") #splitting user input at the "::" so we can store the player number and time as key and value
    if ans == "END": #breaking loop once user enters the required end command
        print("")
        break
    elif len(new) != 2 or new[0] == "" or new[1] == "" or new[1].isdigit() == False or new[0] in list(data.keys()) or int(new[1]) < 0: #once again, checking to see the user has input valid value
            print("Error in data stream. Ignorning. Carry on.")
    else: #storing data in dicionary if all necessary conditions are met
        data[new[0]] = int(new[1]) 
    
if data: #going with the process only if we have valid inputs
    
    #making different lists for keys and values in the dictionary
    time_list = list(data.values()) 
    player_list = list(data.keys())
    
    #calculating the total, average, slowest time, fastest time and fastest runners
    total = len(time_list)
    average = sum(time_list) / len(time_list)
    slow = max(time_list)
    fast = min(time_list)
    fastest = time_list.index(fast)
    
    def mins(m):
        '''A function to check the grammar as according to the number of minutes'''
        if m > 60:
            m = int(m // 60)
            if m == 1:
                return str(m) + " minute"
            else:
                return str(m) + " minutes"
        else:
            return "0 minutes"
    
    def secs_G(sec):
        '''A function to check the grammar as according to the number of seconds'''
        if sec == 1:
            return str(sec) + " second"
        else:
            return str(sec) + " seconds"
    
    def secs(s):
        '''A function to check the number of seconds'''
        if s > 60:
            s = int(s % 60)
            return secs_G(s)
        else:
            return secs_G(s)

    timings = [average, fast, slow] #creating a list with all the required timings
    minutes = list(map(mins,timings)) #creating a list by iterating all the timings through the function that checks the number of minutes
    seconds = list(map(secs,timings)) #creating a list by iterating all the timings through the function that checks the number of seconds
    
    #printing the results
    print("Total runners:", total)
    print(f"Average time: {minutes[0]} and {seconds[0]}")
    print(f"Fastest time: {minutes[1]} and {seconds[1]}")
    print(f"Slowest time: {minutes[2]} and {seconds[2]}")
    print(f"\nBest Time Here: Runner #{player_list[fastest]}")
    
else: #printing error when there's no data
    print("No data found. Nothing to do. What a pity.")