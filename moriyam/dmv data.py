# ==========================================================
# SECTION 1 : IMPORT LIBRARIES
# ==========================================================
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ==========================================================
# SECTION 2 : LOAD CSV FILE
# ==========================================================
df = pd.read_csv("Companies_dataset.csv")

# View first rows
print(df.head())

# ==========================================================
# SECTION 3 : DATA PREPROCESSING
# ==========================================================

# Remove unwanted index column if present
df.drop(columns=['Unnamed: 0'], errors='ignore', inplace=True)

# -------- Clean Ratings --------
df['ratings'] = pd.to_numeric(df['ratings'], errors='coerce')

# -------- Clean Review Count --------
df['review_count'] = df['review_count'].str.replace("(", "")
df['review_count'] = df['review_count'].str.replace(" Reviews)", "")
df['review_count'] = df['review_count'].str.replace("k", "")
df['review_count'] = pd.to_numeric(df['review_count'], errors='coerce') * 1000

# -------- Clean Years --------
df['years'] = df['years'].str.replace(" years old", "")
df['years'] = pd.to_numeric(df['years'], errors='coerce')

# -------- Clean HQ --------
df['hq_place'] = df['hq'].str.split(",").str[0]

# -------- Keep only first 15 companies --------
df = df.head(15)

print(df)

# ==========================================================
# SECTION 4 : QUESTION 1
# FIND HEADQUARTER PLACE NAMES OF COMPANY
# ==========================================================

print("\nHeadquarter Places:\n")
print(df[['name', 'hq_place']])

# ==========================================================

# ==========================================================
# SECTION 5 : QUESTION 3
# BAR CHART [COMPANIES YEAR WISE]
# ==========================================================

plt.figure(figsize=(12,6))
sns.barplot(x='name', y='years', data=df)
plt.title("Companies Year Wise")
plt.xticks(rotation=45)
plt.show()

# ==========================================================
# SECTION 6 : QUESTION 4
# LINE CHART [COMPANIES RATING WISE]
# ==========================================================

plt.figure(figsize=(12,6))
plt.plot(df['name'], df['ratings'], marker='o')
plt.title("Companies Rating Wise")
plt.xticks(rotation=45)
plt.show()

# ==========================================================
# SECTION 7 : QUESTION 5
# PIE CHART [COMPANIES EMPLOYEES WISE]
# ==========================================================

# Convert employee categories to numeric approx values
def emp_convert(x):
    if "1 Lakh+" in str(x):
        return 100000
    elif "50k" in str(x):
        return 50000
    else:
        return 10000

df['emp_num'] = df['employees'].apply(emp_convert)

plt.figure(figsize=(10,10))
plt.pie(df['emp_num'],
        labels=df['name'],
        autopct='%1.1f%%',
        startangle=90)
plt.title("Companies Employees Wise")
plt.show()

# ==========================================================
# SECTION 8 : FINAL DASHBOARD (ALL CHARTS TOGETHER)
# ==========================================================

fig, axs = plt.subplots(2,2, figsize=(15,10))

# Bar Chart
sns.barplot(x='name', y='years', data=df, ax=axs[0,0])
axs[0,0].set_title("Year Wise")
axs[0,0].tick_params(axis='x', rotation=45)

# Line Chart
axs[0,1].plot(df['name'], df['ratings'], marker='o')
axs[0,1].set_title("Rating Wise")
axs[0,1].tick_params(axis='x', rotation=45)

# Pie Chart
axs[1,0].pie(df['emp_num'], labels=df['name'], autopct='%1.1f%%')
axs[1,0].set_title("Employees Wise")

# Review Count Bar
sns.barplot(x='name', y='review_count', data=df, ax=axs[1,1])
axs[1,1].set_title("Review Wise")
axs[1,1].tick_params(axis='x', rotation=45)

plt.tight_layout()
plt.show()