
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Creating customer churn dataset
data = {
    'CustomerID': [101, 102, 103, 104, 105, 106, 107, 108],
    'Gender': ['Male', 'Female', 'Male', 'Female',
               'Male', 'Female', 'Male', 'Female'],
    'Age': [25, 30, 45, 35, np.nan, 50, 28, 40],
    'MonthlyCharges': [500, 700, 900, 600, 800, np.nan, 550, 750],
    'Tenure': [12, 24, 36, 18, 10, 48, 15, 30],
    'Churn': ['No', 'Yes', 'No', 'Yes',
              'No', 'Yes', 'No', 'Yes']
}

df = pd.DataFrame(data)

# Display original dataset
print("Original Dataset:")
print(df)

# Checking missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Handling missing values
df['Age'] = df['Age'].fillna(df['Age'].mean())
df['MonthlyCharges'] = df['MonthlyCharges'].fillna(
    df['MonthlyCharges'].mean()
)

# Checking duplicate records
df = df.drop_duplicates()

# Summary statistics
print("\nSummary Statistics:")
print(df.describe())

# Churn analysis
print("\nCustomer Churn Count:")
print(df['Churn'].value_counts())

# Average monthly charges by churn
print("\nAverage Monthly Charges:")
print(df.groupby('Churn')['MonthlyCharges'].mean())

# Visualization 1: Churn Count
sns.countplot(x='Churn', data=df)
plt.title("Customer Churn Count")
plt.show()

# Visualization 2: Age Distribution
plt.hist(df['Age'], bins=5)
plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Number of Customers")
plt.show()

# Visualization 3: Monthly Charges
sns.boxplot(x='Churn', y='MonthlyCharges', data=df)
plt.title("Monthly Charges vs Churn")
plt.show()

print("\nEDA Completed Successfully!")
