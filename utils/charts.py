import plotly.express as px


def funding_vs_valuation(df):

    fig = px.scatter(
        df,
        x="Funding Amount (M USD)",
        y="Valuation (M USD)",
        color="Industry",
        size="Employees",
        hover_name="Startup Name",
        title="Funding vs Valuation"
    )

    return fig


def industry_revenue_chart(df):

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

    return fig


def profitability_chart(df):

    profit = (
        df.groupby("Profitable")
        .agg({
            "Revenue (M USD)": "mean",
            "Valuation (M USD)": "mean"
        })
        .reset_index()
    )

    fig = px.bar(
        profit,
        x="Profitable",
        y=[
            "Revenue (M USD)",
            "Valuation (M USD)"
        ],
        barmode="group"
    )

    return fig


def region_funding_chart(df):

    region = (
        df.groupby("Region")
        ["Funding Amount (M USD)"]
        .sum()
        .reset_index()
    )

    fig = px.bar(
        region,
        x="Region",
        y="Funding Amount (M USD)",
        color="Region"
    )

    return fig


def exit_status_chart(df):

    fig = px.pie(
        df,
        names="Exit Status",
        title="Startup Exit Status"
    )

    return fig
