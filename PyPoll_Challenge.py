import csv
import os

file_to_load = os.path.join('Resources/election_results.csv')
file_to_save = os.path.join('Analysis',"election_analysis.txt")

total_votes = 0
candidate_options = []
candidate_votes = {}
county_options = []
county_votes = {}

winning_candidate = ""
winning_count = 0
winnning_percentage = 0

winning_county = ""
county_Wcount = 0
county_Wpercentage = 0

dashs = f"--------------------------------------------\n"

with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    headers = next(file_reader)
    
    for row in file_reader:
        total_votes += 1
        candidate_name = row[2]
        county_name = row[1]

        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name] = 0

        candidate_votes[candidate_name] += 1

        if county_name not in county_options:
            county_options.append(county_name)
            county_votes[county_name] = 0

        county_votes[county_name] += 1

with open(file_to_save, "w") as txt_file:

    election_results = (
        f"\nElection Results\n"
        f"{dashs}"
        f"Total Votes: {total_votes:,}\n"
        f"{dashs}"
        f"County Votes: \n"
    )
    print(election_results, end="")
    txt_file.write(election_results)

    

    for county in county_votes:
        c_votes = county_votes[county]
        c_vote_percentage = (int(c_votes)/int(total_votes))*100

        county_results = (f"{county}: {c_vote_percentage:.1f}% ({c_votes:,})\n")
        txt_file.write(county_results)

        if c_votes > county_Wcount and c_vote_percentage > county_Wpercentage:
            winning_county, county_Wcount, county_Wpercentage = county, c_votes, c_vote_percentage

    county_winning_summary = (
        f"{dashs}"
        f"Largest County Turnout: {winning_county} with {county_Wpercentage:.1f}% ({county_Wcount:,})\n"
        f"{dashs}"
    )

    print(county_winning_summary)
    txt_file.write(county_winning_summary)

    for candidate in candidate_votes:
        votes = candidate_votes[candidate]
        vote_percentage = (int(votes)/int(total_votes))*100

        if votes > winning_count and vote_percentage > winnning_percentage:
            winning_candidate, winning_count, winnning_percentage = candidate, votes, vote_percentage

        candidate_results = (f"{candidate}: {vote_percentage:.1f}% ({votes:,})\n")
        txt_file.write(candidate_results)

    candidate_winning_summary = (
        
        f"{dashs}"
        f"Winner: {winning_candidate}\n"
        f"Winning vote count: {winning_count:,}\n"
        f"Winning percentage: {winnning_percentage:.1f}% \n"
        f"{dashs}"
    )

    print(candidate_winning_summary)
    txt_file.write(candidate_winning_summary)