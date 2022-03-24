import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df= pd.read_excel(r'C:\Users\AMAN KUMAR SINGH\Downloads\NFHS_5_India_Districts_Factsheet_Data.xls', nrows=20, usecols=["State/UT", "Number of Households surveyed","Number of Women age 15-49 years interviewed"])
print(df)

sns.jointplot(x="Number of Households surveyed", y="Number of Women age 15-49 years interviewed", data=df)
plt.show()





