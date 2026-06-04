def generate_insights(df):

    insights = []

    top_industry = (
        df.groupby("Industry")
        ["Revenue (M USD)"]
        .sum()
        .idxmax()
    )

    insights.append(
        f"🏆 Highest revenue industry: {top_industry}"
    )

    top_region = (
        df.groupby("Region")
        ["Valuation (M USD)"]
        .mean()
        .idxmax()
    )

    insights.append(
        f"🌍 Highest valuation region: {top_region}"
    )

    profitability = (
        df["Profitable"]
        .mean() * 100
    )

    insights.append(
        f"📈 {profitability:.2f}% startups are profitable"
    )

    highest_funding = (
        df.sort_values(
            "Funding Amount (M USD)",
            ascending=False
        )
        .iloc[0]
    )

    insights.append(
        f"💰 Most funded startup: {highest_funding['Startup Name']}"
    )

    return insights
