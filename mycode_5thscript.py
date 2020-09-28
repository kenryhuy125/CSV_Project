import csv
from datetime import datetime

import matplotlib.pyplot as plt

open_file = open("death_valley_2018_simple.csv")
open_file2 = open("sitka_weather_2018_simple.csv")
name=''

with open_file as a:
    csv_file = csv.reader(a)
    header_row = next(csv_file)

    print(header_row)
    date_index = header_row.index('DATE')
    high_index = header_row.index('TMAX')
    low_index = header_row.index('TMIN')
    name_index = header_row.index('NAME') 
    
    dates, highs, lows = [], [], []
    
    for row in csv_file:
        if not name:
            name = row[name_index]
            print(name)
            
        the_date = datetime.strptime(row[date_index], '%Y-%m-%d')
        
        try:
            high = int(row[high_index])
            low = int(row[low_index])
            
        except ValueError:
            print(f"Missing data for {the_date}")
            
        else:
            highs.append(high)
            lows.append(low)
            dates.append(the_date)


fig = plt.figure()
fig, ax = plt.subplots(2)

ax[0].set_title('Daily High and Low Temperatures - 2018\nDead Valley')
ax[0].plot(dates, highs, c="red", alpha=0.5)
ax[0].plot(dates, lows, c="blue", alpha=0.5)

open_file2 = open("sitka_weather_2018_simple.csv")
name=''

with open_file2 as b:
    csv_file = csv.reader(b)
    header_row = next(csv_file)

    print(header_row)
    date_index = header_row.index('DATE')
    high_index = header_row.index('TMAX')
    low_index = header_row.index('TMIN')
    name_index = header_row.index('NAME') 
    
    dates, highs, lows = [], [], []
    
    for row in csv_file:
        if not name:
            name = row[name_index]
            print(name)
            
        the_date = datetime.strptime(row[date_index], '%Y-%m-%d')
        
        try:
            high = int(row[high_index])
            low = int(row[low_index])
            
        except ValueError:
            print(f"Missing data for {the_date}")
            
        else:
            highs.append(high)
            lows.append(low)
            dates.append(the_date)

ax[1].set_title('Daily High and Low Temperatures - 2018\nSitka')
ax[1].plot(dates, highs, c="red", alpha=0.5)
ax[1].plot(dates, lows, c="blue", alpha=0.5)

#plt.plot(dates, highs, c="red", alpha=0.5)
#plt.plot(dates, lows, c="blue", alpha=0.5)

plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

#title = f"Daily High and Low Temperatures - 2018\n{name}" 
#plt.title(title)
plt.xlabel('')

fig.autofmt_xdate()

plt.ylabel("Temperature (F)", fontsize = 16)
plt.tick_params(axis = "both", which = "major", labelsize = 16)

plt.show()