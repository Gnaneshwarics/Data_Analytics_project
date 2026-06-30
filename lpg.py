import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
#step 1 : upload the data
data=pd.read_csv("C:\India_lpg_dataset.csv")
#print(data)

#step 2 :  top 5 data will be display
#print (data.head())

#step 3 :  bottom  5 data will be display
#print (data.tail())

#step 4 : transfer the data to x and y  ( y we r doing this : to plot graph )
#x= data.head()
#y = data.tail()
#print(x)
#print(y)

#step 5 :  display the summary of the whole data  ( we get Mean,SD,min,25%,50%,75%,max )
#print(data.describe())

#step 6 : change the columns names
df=data[['Year','Production_MMT','Imports_MMT','Crude_Price_USD','Inflation_Rate']]
df.columns=['Yr','P_MMT','Im_MMT','C_Pr_USD','In_Rate']
#print(df.head())
#print(df.tail())

#step 7:
#today = df[df['Yr'] == 2024]
#print(today)

#step 8:
maxP_MMT = df.sort_values(by='P_MMT', ascending=False)
#print(maxP_MMT)

#step 9 :Slicing

tsd=maxP_MMT[0:5]
print(tsd)
tsd=maxP_MMT[0:10]
print(tsd)

#step 10 :
#sns.barplot(x='Yr', y='P_MMT', data=tsd)
#plt.show()

# step 11 :
sns.barplot(x='Yr',y='P_MMT',data=tsd,hue="Yr")
plt.show()