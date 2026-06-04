import streamlit as st
import pandas as pd
import plotly.express as px

st.title("💰 Funding Analytics")

df = pd.read_csv("startup_data.csv")

col1,col2 = st.columns(2)

with col1:
    fig = px.histogram(
        df,
        x="Funding Amount (M USD)",
        nbins=30,
        title="Funding Distribution"
    )
    st.plotly_chart(fig,use_container_width=True)

with col2:
    fig = px.box(
        df,
        x="Industry",
        y="Funding Amount (M USD)",
        color="Industry",
        title="Industry Funding Spread"
    )
    st.plotly_chart(fig,use_container_width=True)

fig = px.scatter(
    df,
    x="Funding Amount (M USD)",
    y="Revenue (M USD)",
    color="Industry",
    size="Employees",
    title="Funding vs Revenue"
)

st.plotly_chart(fig,use_container_width=True)

top10 = df.nlargest(
    10,
    "Funding Amount (M USD)"
)

st.subheader("Top 10 Funded Startups")
st.dataframe(top10)
