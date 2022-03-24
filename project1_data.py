import seaborn as sns
import matplotlib.pyplot as plt

df= sns.load_dataset("tips")
print(df)

# plt.scatter(x='tip', y='total_bill', data=df)
# sns.scatterplot(x='tip', y='total_bill', data=df, hue='time')

sns.boxplot(y='tip', data=df)
plt.show()
# There is difference between how the boxplot looks when in seaborn and when in matplotlib.

# plt.boxplot(x='tip', data=df)
## Here, it don't take value in y it only takes value of x


# plt.xlabel("Tip", fontsize=12)
# plt.ylabel("Total Bill", fontsize=12)
# plt.title("Tip Vs Total Bill", fontsize=15)
