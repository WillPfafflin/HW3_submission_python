# HW3_submission_python
Python Homework HW3

PyPoll
Created lists for candidates with the provided names and votes that would be appended to later.
With a loop counted all votes into the vote list so I could then count the individual candidate names. 
Could of just did a len function on the votes list but instead did another loop that added 1 for every row in the file. 
After getting a count of all votes per candidate I created dictionary from both the candidate names and votes per candidate. 
A winner was pulled by using a max function on the new dictonary based on most votes.
Changed percentage formating to match given output format. 
Printed the results and then created a write function to output the results to an analysis folder as a txt file.

PyBank
Created blank lists for months, money, and change. 
Addended months and money from a loop to get all the values. Money was converted to an integer as it was getting added.
Did a len function on months to get total months and a sum function on money to get total money. 
Did a loop function to find the monthly change of money. 
Found change average 
Max and min functions on change.
Created a dictionary with the change and month lists so I could pull the max change month and min change month. 
Printed the results and then created a write function to output the results to an analysis folder as a txt file.
