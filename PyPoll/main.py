import os
import csv

candidates = ["Khan","Correy","Li","O'Tooley"]

vote=[]

poll_csv = os.path.join('Resources','02-Homework_03-Python_Instructions_PyPoll_Resources_election_data.csv')

with open(poll_csv) as csvfile:
        
    csvreader = csv.reader(csvfile, delimiter=",")
    
    csv_header = next(csvfile)
    
    for row in csvreader:
        vote.append(row[2]) 

with open(poll_csv) as csvfile:
    
    total_votes = sum(1 for row in csvfile)

    
khan = vote.count("Khan")
correy = vote.count("Correy")
li = vote.count("Li")
otooley = vote.count("O'Tooley")

v_per_c = [khan,correy,li,otooley]

results = dict(zip(v_per_c,candidates))

winner = max(v_per_c)

khan_per = "{:.3%}".format(khan/total_votes)
correy_per = "{:.3%}".format(correy/total_votes)
li_per = "{:.3%}".format(li/total_votes)
otooley_per = "{:.3%}".format(otooley/total_votes)

        
print("Election Results")
print("-------------------------")
print("Total Votes: " + str(total_votes))
print("-------------------------")
print("Khan: " + str(khan_per) + "  " + "(" + str(khan) + ")")
print("Correy: " + str(correy_per) + "  " + "(" + str(correy) + ")")
print("Li: " + str(li_per) + "  " + "(" + str(li) + ")")
print("O'Tooley: " + str(otooley_per) + "  " + "(" + str(otooley) + ")")
print("-------------------------")
print("Winner: " + str(results[winner]))
print("-------------------------")

complete_txt = os.path.join('analysis','PyPoll.txt')

with open(complete_txt,'w') as a:
    print("Election Results", file = a)
    print("-------------------------", file = a)
    print("Total Votes: " + str(total_votes), file = a)
    print("-------------------------", file = a)
    print("Khan: " + str(khan_per) + "  " + "(" + str(khan) + ")", file = a)
    print("Correy: " + str(correy_per) + "  " + "(" + str(correy) + ")", file = a)
    print("Li: " + str(li_per) + "  " + "(" + str(li) + ")", file = a)
    print("O'Tooley: " + str(otooley_per) + "  " + "(" + str(otooley) + ")", file = a)
    print("-------------------------", file = a)
    print("Winner: " + str(results[winner]), file = a)
    print("-------------------------", file = a)