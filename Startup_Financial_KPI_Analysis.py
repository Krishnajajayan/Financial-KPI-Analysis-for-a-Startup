# Import libraries
import pandas as pd

# Load the dataset
df = pd.read_csv('/content/50_Startups.csv')

# View first few rows
print(df.head())

#View last few rows
print(df.tail())

#Check for null values
df.isnull().sum()

#Check for duplicates
df.duplicated().sum()

df.info()

df.describe()

# Rename columns for easier use
df.columns = ['R&D_Spend', 'Administration', 'Marketing_Spend', 'State', 'Profit']

# Step 1: Calculate Burn Rate (Monthly Expenses)
df['Burn_Rate'] = (df['R&D_Spend'] + df['Administration'] + df['Marketing_Spend']) / 12

df.head()

# Step 2: Calculate Run Rate (Assume Profit is Monthly, so annualize)
df['Run_Rate'] = df['Profit'] * 12

df.head()

# Step 3: Estimate CAC (Assume 1000 new customers acquired)
df['CAC'] = df['Marketing_Spend'] / 1000

df.head()

# Step 4: Estimate LTV
# Assume: each company has 1000 customers, average customer lifespan = 2 years
avg_monthly_profit_per_customer = df['Profit'] / 1000
customer_lifespan_months = 24
df['LTV'] = avg_monthly_profit_per_customer * customer_lifespan_months

df.head()

# Step 5: LTV to CAC Ratio
df['LTV_CAC_Ratio'] = df['LTV'] / df['CAC']

df.head()

# Step 6 (Optional): Add fictional cohort groups
df['Cohort'] = ['Cohort ' + str(i//5 + 1) for i in range(len(df))]

df.head()

# Export final KPI dataset to CSV
df.to_csv("financial_kpi_output.csv", index=False)

# Preview key columns
print(df[['State', 'Profit', 'Burn_Rate', 'Run_Rate', 'CAC', 'LTV', 'LTV_CAC_Ratio', 'Cohort']].head(10))

df[['State', 'Profit', 'Burn_Rate', 'Run_Rate', 'CAC', 'LTV', 'LTV_CAC_Ratio', 'Cohort']].dtypes
