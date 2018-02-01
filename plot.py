import csv
import matplotlib.pyplot as plt

dates = []
scores = []

with open('cdf.csv') as csvDataFile:
    csvReader = csv.reader(csvDataFile, delimiter='	')
    for row in csvReader:
        dates.append(row[0])
        scores.append(row[1])


plt.plot(dates, scores, 'ro')
plt.show()
print(dates)

print(scores)
'''
## confused 1. I need to know the n in advance to define k.
##   2. shold I import the sliding window or give the data a weight depending on time.
            considering the time, If in a short period, there are a lot of transaction.
            It may be the unbelievalbe one. this is going to be the problem to find the
            frequent items.
     3. clustering then quantile. here comes another question online clustering. classify the
     customer into groups. then get every a sketch about the data.
    　４．　detect the outliers. can this method work?

'''
