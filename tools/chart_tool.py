import plotly.express as px

def generate_chart(df):
    numeric_cols = df.select_dtypes(include="number").columns

    if len(numeric_cols) < 1:
        return None

    col = numeric_cols[0]

    fig = px.line(df, y=col, title=f"Trend of {col}")

    return fig