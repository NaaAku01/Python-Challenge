import csv
import os

file_to_load=os.path.join(r"PyPoll/Resources/election_data.csv")
#setinitalvariables
total_votes = 0
candidate_votes = {}
results = []
winner = ""
max_votes = 0

with open(file_to_load) as election_data: 
    reader=csv.reader(election_data)

    header=next(reader)

    for row in reader:
        total_votes += 1
        candidate = row[2]

      # Count votes for each candidate
        if candidate not in candidate_votes:
            candidate_votes[candidate] = 0
        candidate_votes[candidate] += 1

#calulatetheaveragechange
for candidate, votes in candidate_votes.items():
    percentage = (votes / total_votes) * 100
    results.append(f"{candidate}: {percentage:.3f}% ({votes})")
    
    if votes > max_votes:
        max_votes = votes
        winner = candidate
#printoutputstatement
output = (
    f"Election results\n"
    f"----------------------------\n"
    f"Total Votes: {total_votes}\n"
    f"----------------------------\n")
for result in results: 
    output += f"{result}\n"
output += (
    f"----------------------------\n"
    f"Winner: {winner} \n"
)
print(output)
#saveoutputstatementastextfile 

