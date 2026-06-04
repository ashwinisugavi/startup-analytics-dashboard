import streamlit as st
import pandas as pd

from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split

st.title("🤖 Startup Valuation Predictor")

df = pd.read_csv("startup_data.csv")

features = [
    "Funding Rounds",
    "Funding Amount (M USD)",
    "Revenue (M USD)",
    "Employees",
    "Market Share (%)"
]

X = df[features]
y = df["Valuation (M USD)"]

X_train,X_test,y_train,y_test = train_test_split(
    X,y,test_size=0.2,
    random_state=42
)

model = RandomForestRegressor(
    n_estimators=300,
    random_state=42
)

model.fit(X_train,y_train)

score = model.score(X_test,y_test)

st.metric(
    "Model R² Score",
    f"{score:.2f}"
)

st.subheader("Predict New Startup")

fund_rounds = st.number_input(
    "Funding Rounds",
    1,20,5
)

funding = st.number_input(
    "Funding Amount (M USD)",
    1.0,500.0,50.0
)

revenue = st.number_input(
    "Revenue (M USD)",
    1.0,1000.0,100.0
)

employees = st.number_input(
    "Employees",
    1,100000,500
)

market_share = st.number_input(
    "Market Share %",
    0.0,100.0,5.0
)

if st.button("Predict Valuation"):

    pred = model.predict([[
        fund_rounds,
        funding,
        revenue,
        employees,
        market_share
    ]])

    st.success(
        f"Estimated Valuation = ${pred[0]:,.2f} Million"
    )
