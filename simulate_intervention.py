import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load Data
print("Loading Diabetes Intervention Data...")
df = pd.read_csv("diabetes_data.csv")

# 1. Calculate HbA1c Reduction
df['HbA1c_Reduction'] = df['Baseline_HbA1c'] - df['Post_Intervention_HbA1c']

# 2. Visualize Pre vs Post HbA1c based on Intervention
melted_df = pd.melt(df, id_vars=['Patient_ID', 'Intervention_Type'], 
                    value_vars=['Baseline_HbA1c', 'Post_Intervention_HbA1c'],
                    var_name='Timepoint', value_name='HbA1c_Level')

plt.figure(figsize=(9, 6))
sns.lineplot(x='Timepoint', y='HbA1c_Level', hue='Intervention_Type', data=melted_df, marker='o', errorbar=None)
plt.title('HbA1c Levels: Baseline vs Post-Intervention (12 Weeks)')
plt.ylabel('HbA1c (%)')
plt.savefig('hba1c_reduction.png')
print("Saved plot: hba1c_reduction.png")

# 3. Analyze Medication Reduction Probability
med_reduction_rates = df.groupby('Intervention_Type')['Medication_Reduced'].value_counts(normalize=True).unstack().fillna(0)
print("\n--- Medication Reduction Probability ---")
print(med_reduction_rates)

# 4. Carbohydrate Intake vs HbA1c Reduction
plt.figure(figsize=(7, 5))
sns.regplot(x='Avg_Daily_Carbs_g', y='HbA1c_Reduction', data=df, color='green')
plt.title('Daily Carbohydrate Intake vs HbA1c Reduction')
plt.xlabel('Average Daily Carbs (g)')
plt.ylabel('Reduction in HbA1c (%)')
plt.savefig('carbs_vs_reduction.png')
print("Saved plot: carbs_vs_reduction.png")
