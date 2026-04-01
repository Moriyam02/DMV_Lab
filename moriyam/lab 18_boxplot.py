import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv("finance_dataset.csv")


df = df[df["Revenue"] < 200000]


df["Revenue"].fillna(df["Revenue"].mean(), inplace=True)
df["EPS"].fillna(df["EPS"].mean(), inplace=True)
df["Expenses"].fillna(df["Expenses"].mean(), inplace=True)


cols = ["Revenue", "Expenses", "Profit", "Assets", "Debt", "ROI", "ROE", "EPS"]


sns.set(style="whitegrid")


plt.figure(figsize=(12, 6))
sns.boxplot(data=df[cols])


plt.xticks(rotation=45)


plt.title("Box Plot of Financial Features")


plt.show()