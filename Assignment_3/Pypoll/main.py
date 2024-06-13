import os
import csv

current_directory = os.getcwd()
filename = os.path.join("election_data.csv")
print(filename) 

candidate_votes = {}


with open(filename, 'r') as file:
    csv_reader = csv.reader(file, delimiter=',')
    
    next(csv_reader, None)  
    total_votes = 0
    for row in csv_reader:
        total_votes += 1
        candidate = row[2] 
        if candidate in candidate_votes:
            candidate_votes[candidate] += 1
        else:
            candidate_votes[candidate] = 1


percentages = {candidate: (votes / total_votes) * 100 for candidate, votes in candidate_votes.items()}


winner = max(percentages, key=percentages.get)


print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
for candidate, votes in candidate_votes.items():
    print(f"{candidate}: {percentages[candidate]:.3f}% ({votes})")
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")
