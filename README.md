📊 GLP-1 Outcomes Modeling Dashboard

🧪 Project Overview

This interactive dashboard models the financial impact of GLP-1 medication use across various levels of member adherence and plan demographics. Built using Streamlit and Python, it allows users to simulate cost outcomes under different population and adherence scenarios, supporting data-driven strategy for employers, payers, and consultants navigating the evolving landscape of obesity and diabetes care.

⸻

🎯 Objectives
	•	Estimate the total cost impact (drug + medical cost offsets) of GLP-1 medications like Wegovy, Zepbound, and Saxenda.
	•	Model changes over a 3-year time horizon using adherence-based medical cost adjustments.
	•	Provide adjustable parameters such as:
	•	Population size
	•	Percent of members eligible for GLP-1s
	•	Drug selection and adherence tier
	•	Timeframe (Year 1–3 cost modeling)

🔍 Key Assumptions
Variable
Value
% of overweight/obese members on GLP-1s
19%
Drug costs per year per member:
Wegovy: $5,000–$7,000Zepbound: $2,000–$3,000Saxenda: $2,000–$5,000
Medical cost impact (vs baseline):
Adherent (≥65% PDC): ↓31%Non-adherent (<20% PDC): ↑34%
GLP-1 population uptake
Adjustable (start with 1–5% of total members)
Time horizon
3 years
Baseline annual medical cost per member
$10,000 (default, editable)

🛠️ Tools & Technologies
	•	Python (Pandas, NumPy)
	•	Streamlit (interactive frontend)
	•	Matplotlib / Plotly (charts)
	•	Git/GitHub (version control)

⸻

📈 How It Works

Users adjust sliders and dropdowns to define:
	•	Plan size
	•	Drug choice
	•	Percent adherence
	•	Expected member uptake

The app then calculates:
	•	Total drug costs per year
	•	Medical cost offsets (or increases)
	•	Cumulative cost impact over 3 years
	•	Comparison charts by drug and adherence level

🚀 Getting Started

🔧 Prerequisites
	•	Python 3.9+
	•	pip install streamlit pandas numpy

💡 Why This Matters

GLP-1 medications are revolutionizing obesity and diabetes care—but they come at a high cost. This tool helps stakeholders:
	•	Model financial tradeoffs across adherence levels
	•	Estimate ROI over time
	•	Explore strategic coverage policies grounded in data