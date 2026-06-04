from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split


def train_model(df):

    features = [
        "Funding Rounds",
        "Funding Amount (M USD)",
        "Revenue (M USD)",
        "Employees",
        "Market Share (%)"
    ]

    X = df[features]

    y = df["Valuation (M USD)"]

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42
    )

    model = RandomForestRegressor(
        n_estimators=300,
        random_state=42
    )

    model.fit(X_train, y_train)

    score = model.score(X_test, y_test)

    return model, score


def predict_valuation(
        model,
        funding_rounds,
        funding_amount,
        revenue,
        employees,
        market_share):

    prediction = model.predict([[
        funding_rounds,
        funding_amount,
        revenue,
        employees,
        market_share
    ]])

    return prediction[0]
