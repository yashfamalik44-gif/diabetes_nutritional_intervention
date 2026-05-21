# Diabetes Nutritional Intervention Modeling

## 📌 Project Overview
Type 2 Diabetes management heavily relies on medical nutrition therapy. This project simulates the impact of 12-week dietary interventions (Low-Glycemic, Keto, Standard Control) on patient HbA1c levels and the subsequent probability of reducing pharmacological medication.

## 🔬 Key Objectives
- Analyze the absolute reduction in HbA1c across different diet therapies.
- Model the linear relationship between average daily carbohydrate intake and glycemic improvement.
- Evaluate the success rate of dietary interventions in reducing the need for diabetes medication.

## 📂 Files Included
- `diabetes_data.csv`: Clinical trial simulation data featuring baseline/post-intervention metrics.
- `simulate_intervention.py`: Python code for longitudinal data reshaping and regression analysis.
- Visual outputs (`hba1c_reduction.png`, `carbs_vs_reduction.png`).

## 🛠️ Tools Used
- Python 3, Pandas, Matplotlib, Seaborn

## 🚀 How to Run
```bash
pip install pandas matplotlib seaborn
python simulate_intervention.py
```

## 📊 Findings Summary
- Patients on Low-Glycemic and Ketogenic diets showed a sharp downward trajectory in HbA1c over 12 weeks compared to the control group.
- There is a strong negative correlation between daily carbohydrate intake and HbA1c reduction (i.e., lower carbs yielded higher reductions in HbA1c).
- Over 80% of patients on carbohydrate-restricted interventions were able to reduce their medication dosages.
