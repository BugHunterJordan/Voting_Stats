##Jordan Pangrazzi
##9/24/25
##Process data for a vote, and display the candidates voting stats. Also allow users to search for a specific candidate by name and see their stats

numCand = int(input("How many participants are in the election? (Mimimum 1): "))  #user enters number of candidates
while numCand < 1:   
    numCand = int(input("Invalid entry - enter a valid number of participants (1 or more): "))  #if < 1 candidate will display an error
nameCand = []   #set a list for candidate names
votesCand = []  #set a list for candidate votes
for x in range(numCand):   
    name = input("enter the name of the candidate: ")   
    votes = float(input("enter his/her votes: "))   #for each candidate we will ask the user to enter their name & amount of votes 
    nameCand.append(name)
    votesCand.append(votes)

total = sum(votesCand)   #total is the sum of all candidate votes
avg = total / numCand    #average is the total of votes divided by the number of candidates 
print("Total votes casted = ", format(total, '.2f'))    #display the total of all candidate votes
print("average votes = ", format(avg, '.2f'))      #display the average of all candidate votes

print("\nVOTE RESULTS: 2025\n")

percVotes = []    #set a list for percentage of votes
for v in range(len(votesCand)): 
    perc = (votesCand[v] / total) * 100  #for each vote we will calculate the percentage by dividing the votes by the total, then * 100 to get it into a percentage
    percVotes.append(perc)
    
for x in range(numCand):  
    print(nameCand[x], "\t", votesCand[x], "\t", format(percVotes[x], '.2f'), "%")  #print candidate names, votes, and percentage of votes.

print("\nS E A R C H R E S U L T S\n")

key = input("Enter the participants name to see their vote stats: ")  #allow users to search for a specific candidate by name
found = 0
for x in range(numCand):
    if nameCand[x] == key:   
        print("Candidate", nameCand[x], " received Number of votes: ", votesCand[x], " - Percentage of votes: ", format(percVotes[x], '.2f')) #if candidates name populates we will display their name, amount of votes, and percentage of votes
        found = 1      
if found == 0:
    print(key, "is not a candidate on my list")  #if no candidate is found, display that they are not a candidate on my list
