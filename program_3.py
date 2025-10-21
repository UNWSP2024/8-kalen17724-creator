# Program #3: Capital Quiz
# Write a program that creates a dictionary containing the U.S. states as keys, 
# and their capitals as values.  
# The program should then randomly quiz the user by displaying the name of a state 
# and asking the user to enter the state's capital.  
# The program should count of the number of correct and incorrect responses.  
# (You could alternatively use another country and provinces, 
# or countries of the world and capitals).# or countries of the world and capitals).

import random 


states_capitals = {
    'Alabama' : 'Montgomery', 
    'Alaska' : 'Juneau',
    'Arizona' : 'Phoenix', 
    'Arkansas' : 'Little Rock', 
    'Californa' : 'Sacramento' ,
    'Colorado' : 'Denver' ,
    'Conneticut' : 'Hartford', 
    'Deleware' : 'Dover' ,
    'Florida' : 'Tallahasee',
    'Geargia' : 'Atlanta' ,
    'Hawaii' : 'Honolulu',
    'Idaho' : 'Boise',
    'Illinois' : 'Springfield',
    'Indiana' : 'Indianapolis',
    'Iowa' : 'Des Moines',
    'Kansas' : 'Topeka',
    'Kentucky' : 'Frankfort',
    'Louisiana' : 'Baton Rouge',
    'Maine' : 'Augusta',
    'Maryland' : 'Annapolis',
    'Massachusetts' : 'Boston',
    'Michigan' : 'Lansing',
    'Minnesota' : 'St. Paul',
    'Missisippi' : 'Jackson',
    'Missouri' : 'Jefferson City',
    'Montanna' : 'Helena',
    'Nebraska' : 'Lincoln',
    'Nevada' : 'Carson City',
    'New Hampshire' : 'Concord',
    'New Jersey' : 'Trenton',
    'New Mexico' : 'Santa Fe',
    'New York' : 'Albany',
    'North Carolina' : 'Raleigh',
    'North Dakota' : 'Bismark',
    'Ohio' : 'Columbus',
    'Oklahoma' : 'Oklahoma City',
    'Oregon' : 'Salem',
    'Pennsylvania' : 'Harrisburg',
    'Rhode Island' : 'Providence',
    'South Carolina' : 'Columbia',
    'South Dakota' : 'Pierre',
    'Tennessee' : 'Nashville',
    'Utah' : 'Salt Lake City',
    'Vermont' : 'Montpelier',
    'Virginia' : 'Richmond',
    'Washington' : 'Olympia',
    'West Virginia' : 'Charleston',
    'Wisconsin' : "Madison",
    'Wyoming' : 'Cheyene',
}

name = input("Enter your name: ")
date = input("Enter the date: ")

score = 0
for i in range(10):
    state = random.choice(list(states_capitals.keys()))
    answer = input(f"({i+1}/10)What is the capital of {state}? ").strip()

#Checking if the answer is correct
    if answer.lower() == states_capitals[state].lower():
        print("Correct!\n")
        score +=1
    else:
        print(f"That is incorrect. The capital of {state} is {states_capitals[state]}.\n")

grade = score/10*100

print(name)
print(date)

if grade >=50:
    print("You passed you got: ",score," correct, which is: ",grade,"%")
else:
    print("You failed", name,"you got: ",score," corecct, which is only: ",grade,"%")
    
