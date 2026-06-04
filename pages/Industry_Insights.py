import streamlit as st
import pandas as pd
import plotly.express as px

st.title("🏭 Industry Insights")

df = pd.read_csv("startup_data.csv")

industry_rev = (
    df.groupby("Industry")
    ["Revenue (M USD)"]
    .sum()
    .reset_index()
)

fig = px.bar(
    industry_rev,
    x="Industry",
    y="Revenue (M USD)",
    color="Industry",
    text_auto=True
)

st.plotly_chart(fig,use_container_width=True)

industry_val = (
    df.groupby("Industry")
    ["Valuation (M USD)"]
    .mean()
    .reset_index()
)

fig = px.bar(
    industry_val,
    x="Industry",
    y="Valuation (M USD)",
    color="Industry",
    title="Average Valuation"
)

st.plotly_chart(fig,use_container_width=True)

industry_emp = (
    df.groupby("Industry")
    ["Employees"]
    .sum()
    .reset_index()
)

fig = px.pie(
    industry_emp,
    names="Industry",
    values="Employees",
    title="Employee Share"
)

st.plotly_chart(fig,use_container_width=True)
