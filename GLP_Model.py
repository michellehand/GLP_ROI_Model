import streamlit as st
import pandas as pd

# Title
st.title("GLP-1 Cost Impact Modeling Tool")

# Add summary to the app
st.markdown("""
### GLP-1 Cost Impact Calculation Summary

This tool estimates the **3-year total cost** of GLP-1 usage for an employer health plan, factoring in medication expenses and changes in medical costs due to adherence.
#### **Step-by-Step Calculation Logic:**

1. **Determine Members on GLP-1**  
   We calculate the number of members projected to be on a GLP-1 medication by taking the percentage of individuals who are overweight.
2. **Adjust Medical Costs Based on Adherence**  
GLP-1 adherence affects overall medical cost trajectory:
            **High adherence** reduces medical spend by 31%
            **Low adherence** increases it by 34%
3. **Incorporate Drug Costs**  
Each GLP-1 drug has a 3-year **minimum and maximum** cost range:
            For example, Wegovy = 5,000–7,000 per year
            Total drug cost = annual cost × 3 years
4. **Calculate Total Cost Ranges**
For all members on GLP-1, we estimate the 3-year cost as:
The adjusted medical cost over 3 years:
#### **Outputs:**
**Members on GLP-1**: Based on plan size and uptake rate  
**Min Total Cost**: Conservative estimate using lower drug cost  
**Max Total Cost**: Upper-bound estimate using higher drug cost
""")

# Inputs
plan_size = st.number_input("Plan Size (Number of Members)", min_value=100, max_value=1000000, value=10000)
percent_on_glp1 = st.slider("Percent of Overweight Members on GLP-1", 0.0, 100.0, 19.0) / 100
base_medical_cost = st.number_input("Base Yearly Medical Cost", min_value=0, max_value=1000000, value=10000)
drug_selected = st.selectbox("Select GLP-1 Drug", ["Wegovy", "Zepbound", "Saxenda"])
adherence_level = st.selectbox("Adherence Level", ["High (>=65% PDC)", "Low (<20% PDC)"])

# Assumptions
drug_costs = {
    "Wegovy": (5000, 7000),
    "Zepbound": (2000, 3000),
    "Saxenda": (2000, 5000)
}

adherence_impact = {
    "High (>=65% PDC)": -0.31,
    "Low (<20% PDC)": 0.34
}

# Calculations
min_drug_cost, max_drug_cost = drug_costs[drug_selected]
adherence_effect = adherence_impact[adherence_level]
members_on_glp1 = int(plan_size * percent_on_glp1)

results = []

med_cost_total = base_medical_cost * (1 + adherence_effect) * 3
total_min_cost = members_on_glp1 * (med_cost_total + min_drug_cost * 3)
total_max_cost = members_on_glp1 * (med_cost_total + max_drug_cost * 3)
results.append({
        "Members on GLP-1": members_on_glp1,
        "Min Total Cost": total_min_cost,
        "Max Total Cost": total_max_cost
    })

# Display
results_df = pd.DataFrame(results)
st.write("### Projected 3-Year Total Cost Impact")
st.dataframe(results_df)