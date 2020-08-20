import datetime
from matplotlib import pyplot as plt
import matplotlib.dates as mdates

filename = "weightInfos.txt"

lines = []
with open(filename, "r") as f:
	f.readline()
	lines = f.readlines()

dates = []
weight = []
fat = []
muscle = []
for line in lines:
	splitted_line = line.split()
	dates.append(splitted_line[3].replace("\n",""))
	weight.append(splitted_line[0])
	fat.append(splitted_line[1])
	muscle.append(splitted_line[2])
	
dates_values = [datetime.datetime.strptime(d,"%d/%m/%Y").date() for d in dates]

plt.figure("Weight")

ax = plt.gca()
formatter = mdates.DateFormatter("%Y-%m-%d")
ax.xaxis.set_major_formatter(formatter)
locator = mdates.DayLocator()
ax.xaxis.set_major_locator(locator)
plt.xlabel("date")

plt.figure("Weight")
plt.title('Weight')
plt.ylabel("weight in kg")
plt.plot(dates_values, weight)

plt.figure("Fat")
plt.title('Fat')
plt.ylabel("fat in percentage")
plt.plot(dates_values, fat)

plt.figure("Muscle")
plt.title('Muscle')
plt.ylabel("muscle in percentage")
plt.plot(dates_values, muscle)
plt.show()