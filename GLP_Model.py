import streamlit as st
import pandas as pd

# Title
st.title("GLP-1 Cost Impact Modeling Tool")

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