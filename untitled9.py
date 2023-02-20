from IPython.display import Image
Image(filename = 'Map.png')

Developed Countries refers to the sovereign (independent) nation/state whose economy has highly progressed and possesses great technological infrastructure, as compared to other nations. The countries with low industrialization and low human development index are termed as developing countries.

import pandas as pd
import matplotlib.pyplot as plt 
df = pd.read_csv('Data.csv')
df

Australia = df.loc[df['Country'] == 'Australia']
Australia

Italy = df.loc[df['Country'] == 'Italy']
Italy

Brazil = df.loc[df['Country'] == 'Brazil']
Brazil

Colombia = df.loc[df['Country'] == 'Colombia']
Colombia

fig = plt.subplots(figsize = (10, 10))
label = Australia['Year']
value = Australia['Total expenditure']
plt.plot(label, value, label = "Australia", linewidth = 3.0)
label = Italy['Year']
value = Italy['Total expenditure']
plt.plot(label, value, label = "Italy", linewidth = 3.0)
label = Brazil['Year']
value = Brazil['Total expenditure']
plt.plot(label, value, label = "Brazil", linewidth = 3.0)
label = Colombia['Year']
value = Colombia['Total expenditure']
plt.plot(label, value, label = "Colombia", linewidth = 3.0)
plt.xlabel("Years")
plt.ylabel("Total Expenditure")
plt.title("Total Expenditure on Health of Developed & Developing Countries")
plt.legend()
plt.show()

#Task 2
from IPython.display import Image
Image(filename = 'Map2.png')

The term “life expectancy” refers to the number of years a person can expect to live. By definition, life expectancy is based on an estimate of the average age that members of a particular population group will be when they die.

fig = plt.subplots(figsize = (10, 10))
label = Australia['Year']
value = Australia['Life expectancy']
plt.plot(label, value, label = "Australia", linewidth = 3.0)
label = Italy['Year']
value = Italy['Life expectancy']
plt.plot(label, value, label = "Italy", linewidth = 3.0)
label = Brazil['Year']
value = Brazil['Life expectancy']
plt.plot(label, value, label = "Brazil", linewidth = 3.0)
label = Colombia['Year']
value = Colombia['Life expectancy']
plt.plot(label, value, label = "Colombia", linewidth = 3.0)
plt.xlabel("Years")
plt.ylabel("Life Expectancy")
plt.title("Higher Life Expectancy of Developed & Developing Countries")
plt.legend()
plt.show()