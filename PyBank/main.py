import os 
import csv

#variables
months = 0
pl = 0 
maxpl = 0
minpl = 0

#get file
budp = os.path.join('Resources', 'budget_data.csv')

#open file
with open(budp) as budfh:
    budf = csv.reader(budfh, delimiter=',')
    budh = next(budf)

    #loop to sum months and profit/loss
    for x in budf:
        months = months +1
        pl = pl + int(x[1])
        #ID Max and MIN profit/loss and relative months
        if int(x[1]) > int(maxpl):
            maxpl = int(x[1]) 
            maxplm = x[0]
        elif int(x[1]) < int(minpl):
            minpl = int(x[1]) 
            minplm = x[0]

#Format output to $$
pld = "${:,.2f}".format(pl)
avechange = pl / months
avechanged = "${:,.2f}".format(avechange)
maxpld = "${:,.2f}".format(maxpl)
minpld = "${:,.2f}".format(minpl)

#print statements
print("Total Months: " + str(months))
print("Total: " + str(pld))
print("Average Change: " + str(avechanged))
print("Greatest Increase in Profits: " + str(maxplm) + ": " + str(maxpld))
print("Greatest Decrease in Profits: " + str(minplm) + ": " + str(minpld))

#assign output path
output_path = os.path.join("Analysis" , "banksummary.txt")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w') as textfile:

    # Initialize csv.writer
    textwriter = csv.writer(textfile, delimiter=',')

    # Write to the text file
    textwriter.writerow(["Total Months: " + str(months)])
    textwriter.writerow(["Total: " + str(pld)])
    textwriter.writerow(["Average Change: " + str(avechanged)])
    textwriter.writerow(["Greatest Increase in Profits: " + str(maxplm) + ": " + str(maxpld)])
    textwriter.writerow(["Greatest Decrease in Profits: " + str(minplm) + ": " + str(minpld)])

