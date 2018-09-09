import os
import csv


# Identifies file with poll data
file = os.path.join('ElectionData', 'Election_Data' + '.csv')

#Create dictionary to be used for candidate name and vote count.
poll = {}

#The total number of votes cast
total_votes = 0

#get data file
with open(file, 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    next(csv_reader, None)

    #count votes for each candidate 
    for row in csv_reader:
        total_votes += 1
        if row[2] in poll.keys():
            poll[row[2]] = poll[row[2]] + 1
        else:
            poll[row[2]] = 1
 
#create empty list for candidates and his/her vote count
candidates = []
vote_count = []

#take dictionaries of keys and values and dump  into the lists
# + candidates and num_votes
for key, value in poll.items():
    candidates.append(key)
    vote_count.append(value)

# create vote% list
vote_percent = []
for n in vote_count:
    vote_percent.append(round(n/total_votes*100, 1))

# candidates, vote count and vote% into tuples
clean_data = list(zip(candidates, vote_count, vote_percent))

# put winners regardless of tie
winner_list = []

for name in clean_data:
    if max(vote_count) == name[1]:
        winner_list.append(name[0])

# make winner list a string with the first entry
winner = winner_list[0]

# run if there is a tie and put extra winners into  string
if len(winner_list) > 1:
    for w in range(1, len(winner_list)):
        winner = winner + ", " + winner_list[w]

#prints file list
output_file = os.path.join('Output', 'election_output' +'.txt')

with open(output_file, 'w') as txtfile:
    txtfile.writelines('Election Results \n------------------------- \nTotal Votes: ' + str(total_votes) + 
      '\n-------------------------\n')
    for entry in clean_data:
        txtfile.writelines(entry[0] + ": " + str(entry[2]) +'%  (' + str(entry[1]) + ')\n')
    txtfile.writelines('------------------------- \nWinner: ' + winner + '\n-------------------------')

#print file into terminal
with open(output_file, 'r') as readfile:
    print(readfile.read())
