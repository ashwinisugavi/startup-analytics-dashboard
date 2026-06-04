import streamlit as st
import pandas as pd
import plotly.express as px

st.title("📊 Executive Dashboard")

df = pd.read_csv("startup_data.csv")

# Sidebar Filters
industry = st.sidebar.multiselect(
    "Industry",
    df["Industry"].unique(),
    default=df["Industry"].unique()
)

region = st.sidebar.multiselect(
    "Region",
    df["Region"].unique(),
    default=df["Region"].unique()
)

df = df[
    (df["Industry"].isin(industry))
    &
    (df["Region"].isin(region))
]

# KPI Cards
c1,c2,c3,c4,c5 = st.columns(5)

c1.metric("Startups", len(df))
c2.metric("Funding", f"${df['Funding Amount (M USD)'].sum():,.0f}M")
c3.metric("Revenue", f"${df['Revenue (M USD)'].sum():,.0f}M")
c4.metric("Avg Valuation", f"${df['Valuation (M USD)'].mean():,.0f}M")
c5.metric("Profit %", f"{df['Profitable'].mean()*100:.1f}%")

st.divider()

fig = px.scatter(
    df,
    x="Funding Amount (M USD)",
    y="Valuation (M USD)",
    size="Employees",
    color="Industry",
    hover_name="Startup Name",
    title="Funding vs Valuation"
)

st.plotly_chart(fig, use_container_width=True)

st.dataframe(df)
