import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

df= pd.read_csv(r'C:\Users\AMAN KUMAR SINGH\Downloads\Height of Male and Female by Country 2022.csv')
print(df)


sns.scatterplot(x='Male Height in Ft', y='Female Height in Ft', data=df)
plt.show()


# Conclusion:
# It shows that data is formed in clusters and are positively correlated as it is increasing...

