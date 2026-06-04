import streamlit as st
import pandas as pd
import plotly.express as px

st.title("📈 Profitability Analysis")

df = pd.read_csv("startup_data.csv")

profit = (
    df.groupby("Profitable")
    .agg({
        "Revenue (M USD)":"mean",
        "Valuation (M USD)":"mean"
    })
    .reset_index()
)

fig = px.bar(
    profit,
    x="Profitable",
    y=["Revenue (M USD)",
       "Valuation (M USD)"],
    barmode="group"
)

st.plotly_chart(fig,use_container_width=True)

fig2 = px.pie(
    df,
    names="Profitable",
    title="Profitability Distribution"
)

st.plotly_chart(fig2,use_container_width=True)

st.subheader("Profitable Startups")

profitable_df = df[df["Profitable"]==True]

st.dataframe(
    profitable_df[
        ["Startup Name",
         "Industry",
         "Revenue (M USD)",
         "Valuation (M USD)"]
    ]
)
