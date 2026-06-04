
import streamlit as st
import pandas as pd
import plotly.express as px

st.title("🌍 Regional Analysis")

df = pd.read_csv("startup_data.csv")

region_funding = (
    df.groupby("Region")
    ["Funding Amount (M USD)"]
    .sum()
    .reset_index()
)

fig = px.bar(
    region_funding,
    x="Region",
    y="Funding Amount (M USD)",
    color="Region"
)

st.plotly_chart(fig,use_container_width=True)

region_revenue = (
    df.groupby("Region")
    ["Revenue (M USD)"]
    .sum()
    .reset_index()
)

fig2 = px.line(
    region_revenue,
    x="Region",
    y="Revenue (M USD)",
    markers=True
)

st.plotly_chart(fig2,use_container_width=True)

fig3 = px.sunburst(
    df,
    path=["Region","Industry"],
    values="Revenue (M USD)"
)

st.plotly_chart(fig3,use_container_width=True)
