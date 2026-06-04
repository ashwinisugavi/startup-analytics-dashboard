import streamlit as st
from utils.data_loader import load_data
from utils.styles import load_css

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="Startup Analytics Dashboard",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# -----------------------------
# Custom CSS
# -----------------------------
load_css()

# -----------------------------
# Load Data
# -----------------------------
df = load_data()

# -----------------------------
# Sidebar
# -----------------------------
st.sidebar.image(
    "assets/logo.png",
    width=150
)

st.sidebar.title("🚀 Startup Analytics")

st.sidebar.info(
    """
    ### Navigation
    
    Use the pages menu above to explore:
    
    📊 Executive Dashboard
    
    💰 Funding Analytics
    
    🏭 Industry Insights
    
    📈 Profitability Analysis
    
    🌍 Regional Analysis
    
    🤖 ML Valuation Predictor
    
    🧠 AI Insights
    """
)

# -----------------------------
# Header
# -----------------------------
st.title("🚀 Startup Analytics Dashboard")

st.markdown("""
### Comprehensive Startup Ecosystem Analysis

Analyze startup performance, funding trends,
industry growth, profitability, regional insights,
and valuation prediction using Machine Learning.
""")

# -----------------------------
# Banner
# -----------------------------
st.image(
    "assets/banner.png",
    use_container_width=True
)

# -----------------------------
# KPI Section
# -----------------------------
st.subheader("📌 Key Metrics")

col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    st.metric(
        "Total Startups",
        len(df)
    )

with col2:
    st.metric(
        "Total Funding",
        f"${df['Funding Amount (M USD)'].sum():,.0f}M"
    )

with col3:
    st.metric(
        "Total Revenue",
        f"${df['Revenue (M USD)'].sum():,.0f}M"
    )

with col4:
    st.metric(
        "Average Valuation",
        f"${df['Valuation (M USD)'].mean():,.0f}M"
    )

with col5:
    st.metric(
        "Profitability Rate",
        f"{df['Profitable'].mean()*100:.2f}%"
    )

# -----------------------------
# Dataset Summary
# -----------------------------
st.divider()

st.subheader("📂 Dataset Overview")

c1, c2 = st.columns(2)

with c1:
    st.write("Rows:", df.shape[0])
    st.write("Columns:", df.shape[1])

with c2:
    st.write("Industries:", df["Industry"].nunique())
    st.write("Regions:", df["Region"].nunique())

# -----------------------------
# Data Preview
# -----------------------------
st.divider()

st.subheader("🔍 Sample Data")

st.dataframe(
    df.head(10),
    use_container_width=True
)

# -----------------------------
# Automated Insights
# -----------------------------
st.divider()

st.subheader("🧠 Quick Insights")

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

top_startup = (
    df.sort_values(
        "Funding Amount (M USD)",
        ascending=False
    )
    .iloc[0]["Startup Name"]
)

col1, col2, col3 = st.columns(3)

with col1:
    st.success(
        f"🏆 Top Revenue Industry: {top_industry}"
    )

with col2:
    st.info(
        f"🌍 Highest Valuation Region: {top_region}"
    )

with col3:
    st.warning(
        f"💰 Most Funded Startup: {top_startup}"
    )

# -----------------------------
# Footer
# -----------------------------
st.divider()

st.markdown(
    """
    ### About Project

    This dashboard provides:

    ✔ Executive Analytics

    ✔ Funding Trends

    ✔ Industry Comparison

    ✔ Profitability Analysis

    ✔ Regional Insights

    ✔ Machine Learning Valuation Prediction

    Built with:
    Streamlit • Pandas • Plotly • Scikit-Learn
    """
)
