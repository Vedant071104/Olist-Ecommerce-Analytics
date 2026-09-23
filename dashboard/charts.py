import plotly.express as px


def monthly_revenue_chart(df):

    fig = px.line(
        df,
        x="month",
        y="revenue",
        markers=True,
        title="Monthly Revenue Trend"
    )

    fig.update_layout(

        title_x=0.02,

        xaxis_title="",

        yaxis_title="Revenue (R$)",

        height=420,

        template="plotly_white"
    )

    return fig