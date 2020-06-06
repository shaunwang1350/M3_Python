import csv
import os

file_to_load = os.path.join('Resources/election_results.csv')
file_to_save = os.path.join('Analysis',"election_analysis.txt")

total_votes = 0
candidate_options = []
candidate_votes = {}

winning_candidate = ""
winning_count = 0
winnning_percentage = 0

dashs = f"------------------------------\n"

with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    headers = next(file_reader)
    
    for row in file_reader:
        total_votes += 1
        candidate_name = row[2]

        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name] = 0

        candidate_votes[candidate_name] += 1

with open(file_to_save, "w") as txt_file:

    election_results = (
        f"\nElection Results\n"
        f"{dashs}"
        f"Total Votes: {total_votes:,}\n"
        f"{dashs}"
    )
    print(election_results, end="")
    txt_file.write(election_results)

    for candidate in candidate_votes:
        votes = candidate_votes[candidate]
        vote_percentage = (int(votes)/int(total_votes))*100

        if votes > winning_count and vote_percentage > winnning_percentage:
            winning_candidate, winning_count, winnning_percentage = candidate, votes, vote_percentage

        candidate_results = (f"{candidate}: {vote_percentage:.2f}% ({votes:,})\n")
        txt_file.write(candidate_results)

    winning_summary = (
        f"{dashs}"
        f"Winner: {winning_candidate}\n"
        f"Winning vote count: {winning_count:,}\n"
        f"Winning percentage: {winnning_percentage:.2f}% \n"
        f"{dashs}"
    )

    print(winning_summary)
    txt_file.write(winning_summary)