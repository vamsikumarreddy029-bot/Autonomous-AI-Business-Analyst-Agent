from tools.analyze_data import analyze_data
from tools.chart_tool import generate_chart
from tools.forecast_tool import forecast


def execute(file):
    # 1. Analyze data
    df, summary = analyze_data(file)

    # 2. Generate chart
    chart = generate_chart(df)

    # 3. Forecast
    forecast_data = forecast(df)

    # 4. Return ALL
    return df, summary, chart, forecast_data