import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Step 1
data = pd.read_csv("C:\Indian_Traffic_Violations.csv")

# Step 2
x = data.head()
y = data.tail()

# Step 3
print(data.describe())

# Step 4
df = data[['Violation_Type','Fine_Amount','Date','Vehicle_Type','Driver_Age']]

df.columns = ['Violation_T','Fine_A','Dt','Vehicle_t','Dri_Age']

print(df.head())
print(df.tail())

# Step 5
maxDate = df.sort_values(by='Dt', ascending=False)

# Step 6
tsd = maxDate[0:10]
print(tsd)

# ---------------- Graph 1 ----------------
plt.figure(figsize=(12,6))
sns.barplot(x='Dt', y='Violation_T', data=tsd, hue='Dt')
plt.title("Top 10 Highest Traffic Fines by State")
plt.xlabel("Date")
plt.ylabel("Fine Amount")
plt.xticks(rotation=45)
plt.show()

