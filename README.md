# GLP-1 Outcomes Modeling Dashboard

## Project Overview

This interactive dashboard models the **financial impact of GLP-1 medication use** (e.g., Wegovy, Zepbound, Saxenda) across different levels of adherence and plan demographics. Built in Python with Streamlit, it allows users to simulate cost outcomes under customizable scenarios.

The goal is to support **employers, payers, and consultants** in understanding the trade-offs of covering GLP-1 drugs within commercial health plans—particularly in the context of obesity and diabetes management.

**Live App**: [Launch the Streamlit App](https://glproimodel-hbouzpyuvbtvmzup4wvfkb.streamlit.app/)

---

## Objectives

- Estimate the total cost impact (drug costs + medical cost offsets) of GLP-1 medications.
- Model changes over a 3-year time horizon using adherence-based medical cost adjustments.
- Provide adjustable inputs including:
  - Plan size
  - Percent of members eligible for GLP-1s
  - Drug selection (Wegovy, Zepbound, Saxenda)
  - Adherence level
  - Time horizon (3-year projection)

---

## Key Assumptions

| Variable                             | Value/Range                          |
|--------------------------------------|--------------------------------------|
| Percent of overweight/obese members on GLP-1s | 19% (adjustable)              |
| Drug costs per year per member       | Wegovy: $5,000–$7,000  <br> Zepbound: $2,000–$3,000 <br> Saxenda: $2,000–$5,000 |
| Medical cost impact vs baseline      | High adherence (≥65% PDC): −31% <br> Low adherence (<20% PDC): +34% |
| GLP-1 uptake                         | Adjustable (default 1–5% of total members) |
| Time horizon                         | 3 years                              |
| Baseline medical cost per member     | $10,000/year (default, editable)     |

---

## Tools & Technologies

- **Python**: Pandas, NumPy
- **Streamlit**: Interactive frontend
- **Matplotlib / Plotly**: Visualization
- **GitHub**: Version control and collaboration

---

## How It Works

Users adjust parameters using sliders and dropdowns to define:
- Plan size and population assumptions
- GLP-1 drug selection
- Adherence level (high vs. low)
- Projected member uptake

The app calculates:
- Annual and cumulative drug costs
- Expected medical cost offsets (or increases)
- Total 3-year impact per drug and adherence level
- Dynamic charts for visual comparison

---

## Getting Started

### Prerequisites

To run locally:

```bash
pip install streamlit pandas numpy matplotlib
streamlit run app.py
```

### Why This Matters

GLP-1 medications are transforming obesity and diabetes care—but they also come with significant costs. This dashboard helps stakeholders:
- Explore financial tradeoffs under real-world scenarios
- Understand the ROI of covering GLP-1s at different adherence levels
- Make informed, data-driven decisions about benefit design and plan policy
