import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt


df= pd.read_csv(r'C:\Users\AMAN KUMAR SINGH\Downloads\data.csv')
print(df)


sns.boxplot(y="views", data=df)
plt.show()
# Conclusion: There are a lot of outliers here in this dataset, which we can analyze using boxplot as shown in the figure.


sns.regplot(x = "views",y = "likes",ci = None,data=df, label=label)
plt.show()
# Conclusion: Here, it is shown that views and likes increase linearly and data is close to each other.


