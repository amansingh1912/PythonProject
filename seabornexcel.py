import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt


df= pd.read_csv(r'C:\Users\AMAN KUMAR SINGH\Downloads\data.csv')
print(df)


sns.boxplot(y="views", data=df)
plt.show()
# Conclusion: There are a lot of outliers here with respect to "views" in this dataset, which we can analyze using boxplot as shown in the figure.


sns.regplot(x = "views",y = "likes",ci = None,data=df)
plt.show()

# There are 2 outliers in the dataset with respect to regplot.
# Conclusion: Here, it is shown that views and likes increase linearly and data is close to each other.


