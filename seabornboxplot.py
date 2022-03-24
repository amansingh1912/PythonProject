import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

df= sns.load_dataset("tips")
print(df)

sns.boxplot(x='day', y='tip',hue='smoker', data=df)
plt.show()

##Outliers should be investigated carefully.
# an outlier is a data point that differs significantly from other observations.

# outlier is an observation of data that does not fit the rest of the data. It is sometimes called an extreme value. When you graph an outlier, it will appear not to fit the pattern of the graph.












































