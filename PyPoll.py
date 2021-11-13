import csv
import os

#Assign a variable for file to open and read
file_to_open=os.path.join("Resources", "election_results.csv")
#Assign a variable for results file to save
file_to_save=os.path.join("Analysis","election_analysis.txt")

#Initialize a variable to hold total votes and set it to 0
total_votes=0
candidate_options=[]
candidate_votes={}

#Add variables to hold winning candidate, count and %
winning_candidate=""
winning_count=0
winning_percentage=0


#Open the election results file in order to read it
with open(file_to_open) as election_data:

    #Read and analyze the data here
    file_reader=csv.reader(election_data)

    #Print the header row
    headers=next(file_reader)
    print(headers)

    #Print each row in the csv file
    for row in file_reader:
        #Increment total_votes by 1
        total_votes +=1
        #get candidate name from each row
        candidate_name=row[2]

        #if the candidate does not match an existing name in the list, 
        if candidate_name not in candidate_options:
            #then add the candidate name to the candidate option list
            candidate_options.append(candidate_name)

            #begin tracking each candidate's vote count
            candidate_votes[candidate_name]=0
    
        #Add a vote to the candidate's count
        candidate_votes[candidate_name] += 1

#for each of the candidates listed in candidate_votes          
for candidate_name in candidate_votes:
    #set votes to the total votes for that candidate
    votes=candidate_votes[candidate_name]
    #calculate vote percentage by dividing each candidate's vote by total votes. format it to 2 decimal places
    vote_percentage = '{:.2f}'.format(float(votes) / float(total_votes) *100)
    
    print(f"{candidate_name}: {float(vote_percentage):.1f}% ({votes:,})\n")

    #Determine winning vote count and candidate
    if (votes > winning_count) and (float(vote_percentage) > float(winning_percentage)):
        #If this is true, set the winning_count to votes and winning_percentage to vote_percentage
        winning_count=votes
        winning_percentage=vote_percentage
        #Set the winning candidate equal to the candidate's name
        winning_candidate=candidate_name

winning_candidate_summary=(
    f"------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {float(winning_percentage):.1f}%\n"
    f"-------------------------\n")
print(winning_candidate_summary)


