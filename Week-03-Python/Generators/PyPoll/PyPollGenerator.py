# -*- coding: UTF-8 -*-
"""Generate PyPoll Data."""

# Incorporated the CSV module
import csv
import random

# Output File Name
file_output_name = "election_data_2.csv"

# Set up the city, county, and candidate parameters (replace to modify dataset)
population = 3521003
starting_id = 10000000
ending_id = 20000000
counties = ["Marsh", "Bamoo", "Raffah", "Trandee", "Queen"]
candidates = ["Khan", "Correy", "Li", "O'Tooley"]

# Weighting factors which are used in the random generator
county_weights = [0.65, 0.1, 0.03, 0.03, 0.20]
candidate_weights = [0.63, 0.20, 0.14, 0.03]

# Generate all of the voting ids
voter_ids = random.sample(range(starting_id, ending_id), population)

# Generate all of the votes (candidates), then shuffle
candidate_probabilities = zip(candidates, candidate_weights)
votes = []

for candidate in candidate_probabilities:
    votes = votes + [candidate[0]] * int(candidate[1] * population)

random.shuffle(votes)

# Generate all of the counties, then shuffle
county_probabilities = zip(counties, county_weights)
county_votes = []

for county in county_probabilities:
    county_votes = county_votes + [county[0]] * int(county[1] * population)

random.shuffle(county_votes)

# Zip voter_id, county, and vote together
election_data = zip(voter_ids, county_votes, votes)

# Write all of the election data to csv
with open(file_output_name, "w", newline="") as datafile:
    writer = csv.writer(datafile)
    writer.writerow(["Voter ID", "County", "Candidate"])
    writer.writerows(election_data)
