import streamlit as st
import pandas as pd

# Define base assumptions
medication_costs = {
    "Wegovy": (5000, 7000),
    "Zepbound": (2000, 3000),
    "Saxenda": (2000, 5000),
}

cost_impact = {
    "Adherent (PDC ≥ 65%)": -0.31,
    "Non-Adherent (PDC < 20%)": 0.34,
}

# UI
st.title("GLP-1 Cost Impact Simulator")

plan_size = st.number_input("Plan Size (Number of Members)", min_value=100, value=1000, step=100)
overweight_pct = 0.19
glp1_users = int(plan_size * overweight_pct)

st.write(f"Estimated GLP-1 users: {glp1_users} (19% of {plan_size})")

adherence_rate = st.slider("Adherence Rate (PDC ≥ 65%)", 0.0, 1.0, 0.6)
non_adherence_rate = 1 - adherence_rate

selected_drug = st.selectbox("Select GLP-1 Medication", list(medication_costs.keys()))
low_cost, high_cost = medication_costs[selected_drug]
drug_cost = st.slider(f"{selected_drug} Annual Cost per Member", low_cost, high_cost, (low_cost + high_cost) // 2)

# Calculations
adherent_members = int(glp1_users * adherence_rate)
non_adherent_members = glp1_users - adherent_members

adherent_total_cost = adherent_members * drug_cost * (1 + cost_impact["Adherent (PDC ≥ 65%)"])
non_adherent_total_cost = non_adherent_members * drug_cost * (1 + cost_impact["Non-Adherent (PDC < 20%)"])
total_cost = adherent_total_cost + non_adherent_total_cost

# Results
st.subheader("Results")
st.write(f"Adherent Members: {adherent_members}")
st.write(f"Non-Adherent Members: {non_adherent_members}")
st.write(f"Total Estimated Cost (including medical offset/increase): ${total_cost:,.2f}")

df = pd.DataFrame({
    "Group": ["Adherent", "Non-Adherent"],
    "Members": [adherent_members, non_adherent_members],
    "Drug Cost/Member": [drug_cost, drug_cost],
    "Cost Impact": [cost_impact["Adherent (PDC ≥ 65%)"], cost_impact["Non-Adherent (PDC < 20%)"]],
    "Total Cost": [adherent_total_cost, non_adherent_total_cost]
})

df["Total Cost"] = df["Total Cost"].round(2)
st.dataframe(df)