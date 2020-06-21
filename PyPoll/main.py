import os 
import csv

#variables
votes = 0
candidates = []
votecount = [0,0,0,0]

#get file
votep = os.path.join('Resources', 'election_data.csv')

#open file
with open(votep) as votefh:
    votef = csv.reader(votefh, delimiter=',')
    voteh = next(votef)
    #add candidates to candidate list and add votes to votecount list
    for x in votef:
        votes = votes +1
        if x[2] not in candidates:
            candidates.append(x[2])
        elif x[2] == candidates[0]:
            votecount[(0)] += 1
        elif x[2] == candidates[1]:
            votecount[1] += 1
        elif x[2] == candidates[2]:
            votecount[2] += 1
        elif x[2] == candidates[3]:
            votecount[3] += 1

#determine max votes and index number
max_votes = max(votecount)
max_index = votecount.index(max_votes)

#print results
print("Election Results:")
print("--------------------")
print("Total Votes: " + str(votes))
print("--------------------")
print(f'{candidates[0]}: {votecount[0]/votes:.3%} ({votecount[0] +1})')
print(f'{candidates[1]}: {votecount[1]/votes:.3%} ({votecount[1] +1})')
print(f'{candidates[2]}: {votecount[2]/votes:.3%} ({votecount[2] +1})')
print(f'{candidates[3]}: {votecount[3]/votes:.3%} ({votecount[3] +1})')
print("--------------------")
print("Winner: " + (candidates[max_index]))
print("--------------------")

#assign output path
output_path = os.path.join("Analysis" , "pollsummary.txt")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w') as textfile:

    # Initialize csv.writer
    textwriter = csv.writer(textfile, delimiter=',')

    # Write to the text file
    textwriter.writerow(["Election Results:"])
    textwriter.writerow(["--------------------"])
    textwriter.writerow(["Total Votes: " + str(votes)])
    textwriter.writerow(["--------------------"])
    textwriter.writerow([f'{candidates[0]}: {votecount[0]/votes:.3%} ({votecount[0] +1})'])
    textwriter.writerow([f'{candidates[1]}: {votecount[1]/votes:.3%} ({votecount[1] +1})'])
    textwriter.writerow([f'{candidates[2]}: {votecount[2]/votes:.3%} ({votecount[2] +1})'])
    textwriter.writerow([f'{candidates[3]}: {votecount[3]/votes:.3%} ({votecount[3] +1})'])
    textwriter.writerow(["--------------------"])
    textwriter.writerow(["Winner: " + (candidates[max_index])])
    textwriter.writerow(["--------------------"])