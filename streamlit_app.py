import streamlit as st
import pandas as pd
from utils.data_loader import load_data
from utils.styles import load_css

# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------

st.set_page_config(
    page_title="Startup Analytics Dashboard",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --------------------------------------------------
# CUSTOM CSS
# --------------------------------------------------

load_css()

# --------------------------------------------------
# LOAD DATA
# --------------------------------------------------

df = load_data()

# --------------------------------------------------
# SIDEBAR
# --------------------------------------------------

st.sidebar.image(
    "assets/logo.png",
    width=150
)

st.sidebar.title("🚀 Startup Analytics")

st.sidebar.markdown("---")

st.sidebar.success(
    """
    ### Features

    ✔ Executive Dashboard

    ✔ Funding Analytics

    ✔ Industry Insights

    ✔ Profitability Analysis

    ✔ Regional Analysis

    ✔ ML Valuation Predictor

    ✔ AI Business Insights
    """
)

# --------------------------------------------------
# MAIN HEADER
# --------------------------------------------------

st.title("🚀 Startup Analytics Dashboard")

st.markdown(
"""
Analyze startup ecosystem performance using:

- Funding Analysis
- Revenue Analytics
- Industry Benchmarking
- Regional Insights
- Startup Profitability
- Machine Learning Predictions
"""
)

# --------------------------------------------------
# BANNER
# --------------------------------------------------

try:
    st.image(
        "assets/banner.png",
        use_container_width=True
    )
except:
    st.info("Banner image not found.")

# --------------------------------------------------
# KPI SECTION
# --------------------------------------------------

st.markdown("## 📊 Executive Summary")

col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    st.metric(
        "Startups",
        len(df)
    )

with col2:
    st.metric(
        "Funding",
        f"${df['Funding Amount (M USD)'].sum():,.0f}M"
    )

with col3:
    st.metric(
        "Revenue",
        f"${df['Revenue (M USD)'].sum():,.0f}M"
    )

with col4:
    st.metric(
        "Avg Valuation",
        f"${df['Valuation (M USD)'].mean():,.0f}M"
    )

with col5:
    st.metric(
        "Profitability",
        f"{df['Profitable'].mean()*100:.2f}%"
    )

# --------------------------------------------------
# DATASET OVERVIEW
# --------------------------------------------------

st.markdown("---")

st.markdown("## 📂 Dataset Overview")

c1, c2, c3 = st.columns(3)

with c1:
    st.metric(
        "Rows",
        df.shape[0]
    )

with c2:
    st.metric(
        "Columns",
        df.shape[1]
    )

with c3:
    st.metric(
        "Industries",
        df["Industry"].nunique()
    )

# --------------------------------------------------
# COLUMN DETAILS
# --------------------------------------------------

st.markdown("## 📝 Dataset Features")

column_info = pd.DataFrame(
    {
        "Column": df.columns,
        "Data Type": df.dtypes.astype(str)
    }
)

st.dataframe(
    column_info,
    use_container_width=True
)

# --------------------------------------------------
# DATA PREVIEW
# --------------------------------------------------

st.markdown("## 🔍 Data Preview")

st.dataframe(
    df.head(15),
    use_container_width=True
)

# --------------------------------------------------
# QUICK INSIGHTS
# --------------------------------------------------

st.markdown("---")
st.markdown("## 🧠 Quick Business Insights")

top_industry = (
    df.groupby("Industry")
    ["Revenue (M USD)"]
    .sum()
    .idxmax()
)

top_region = (
    df.groupby("Region")
    ["Valuation (M USD)"]
    .mean()
    .idxmax()
)

top_funded = (
    df.sort_values(
        "Funding Amount (M USD)",
        ascending=False
    )
    .iloc[0]["Startup Name"]
)

profit_rate = (
    df["Profitable"].mean()*100
)

col1, col2 = st.columns(2)

with col1:
    st.success(
        f"🏆 Highest Revenue Industry: {top_industry}"
    )

    st.info(
        f"🌎 Highest Valuation Region: {top_region}"
    )

with col2:
    st.warning(
        f"💰 Most Funded Startup: {top_funded}"
    )

    st.success(
        f"📈 Profitability Rate: {profit_rate:.2f}%"
    )

# --------------------------------------------------
# NAVIGATION HELP
# --------------------------------------------------

st.markdown("---")

st.markdown(
"""
## 📌 Explore More

Use the left sidebar pages to explore:

| Page | Purpose |
|--------|----------|
| Executive Dashboard | Overall KPIs |
| Funding Analytics | Funding trends |
| Industry Insights | Industry comparisons |
| Profitability Analysis | Profit vs Loss |
| Regional Analysis | Region-wise analytics |
| ML Predictor | Predict startup valuation |
| AI Insights | Automated business insights |
"""
)

# --------------------------------------------------
# FOOTER
# --------------------------------------------------

st.markdown("---")

st.caption(
    "Built with Streamlit, Plotly, Pandas and Scikit-Learn"
)
