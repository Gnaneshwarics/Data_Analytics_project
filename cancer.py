#step 1
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Upload the dataset
data = pd.read_csv("C:\india_cancer_patients_2022_2025.csv")
#print(data)

#step 2
# .head() is used to print top 5 records
x = data.head()
y = data.tail()

# .tail() is used to print last 5 records

#print(data.describe())

#step 3
df = data[['Age','Gender','State','Cancer_Type','Stage']]

df.columns = ['Age','Gen','State','Cancer','Stage']

#print(df.head())
#print(df.tail())

#step 4
today = df[df.Gen == 'Female']
print(today.head())

#step 5
maxdt = today.sort_values(by='Age', ascending=False)
print(maxdt)

#step 6 (Slicing)
tsd = maxdt[0:5]
print(tsd)

tsd = maxdt[0:10]
print(tsd)

#step 7
sns.barplot(x='State', y='Age', data=tsd, hue='State')
plt.xticks(rotation=45)
plt.show()