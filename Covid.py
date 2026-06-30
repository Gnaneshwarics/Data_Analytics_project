#step 1
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
data=pd.read_csv("C:\\Users\\Admin\\Downloads\\archive (1)\\covid_19_india.csv")
#print(data)

#step 2
#.head is used to print top 5 records
x=data.head()
y=data.tail()
#.tail is used to print last 5 records

#print(data.describe())
df=data[['Date','Time','State/UnionTerritory','Cured','Deaths','Confirmed'
]]
df.columns=['Dt','Ti','St/Ut','Cure','Death','Conf']
#print(df.head())
#print(df.tail())

today=df[df.Dt=='2020-03-14']
print(today.head())

maxdt=today.sort_values(by='Death',ascending=False)
print(maxdt)
#slicing
tsd=maxdt[0:5]
print(tsd)
tsd=maxdt[0:10]
print(tsd)

sns.barplot(x='St/Ut',y='Conf',data=tsd,hue="St/Ut")
plt.show()