import os
import csv

months=[]
money=[]
change=[0]

bank_csv = os.path.join('Resources', '02-Homework_03-Python_Instructions_PyBank_Resources_budget_data.csv')

with open(bank_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    csv_header = next(csvfile)
    
    for row in csvreader:
        months.append(row[0])
        money.append(int(row[1]))
        
        
        month_count = len(months)
        total_money = "${:}".format(sum(money))

change.extend([ + money[x+1]-money[x] for x in range(len(money)-1)])

change_avg = "${:.2f}".format(sum(change)/(len(change)-1))


max_increase =max(change)
max_decrease =min(change)

max_increase_format= ("(" + "${:}".format(max_increase) +")")
max_decrease_format= ("(" + "${:}".format(max_decrease) +")")

change_by_month = dict(zip(change,months))


print("Financial Analysis")
print("----------------------------")
print("Total Months:" + str(month_count))
print("Total:" + str(total_money))
print ("Average Change:" + str(change_avg))
print ("Greatest Increase in Profits:" + str(change_by_month[max_increase]) + str(max_increase_format))
print ("Greatest Decrease in Profits:" + str(change_by_month[max_decrease]) + str(max_decrease_format))

complete_txt = os.path.join('analysis','PyBank.txt')

with open(complete_txt,'w') as a:
    print("Financial Analysis", file = a)
    print("----------------------------", file = a)
    print("Total Months:" + str(month_count), file = a)
    print("Total:" + str(total_money), file = a)
    print ("Average Change:" + str(change_avg), file = a)
    print ("Greatest Increase in Profits:" + str(change_by_month[max_increase]) + str(max_increase_format), file = a)
    print ("Greatest Decrease in Profits:" + str(change_by_month[max_decrease]) + str(max_decrease_format), file = a)