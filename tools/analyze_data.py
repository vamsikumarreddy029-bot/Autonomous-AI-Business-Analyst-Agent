import pandas as pd

def analyze_data(file):
    df = pd.read_csv(file)

    # Basic info
    summary = {
        "rows": df.shape[0],
        "columns": list(df.columns),
        "missing_values": df.isnull().sum().to_dict(),
    }

    # Numeric analysis
    numeric_cols = df.select_dtypes(include="number").columns

    if len(numeric_cols) > 0:
        summary["statistics"] = df[numeric_cols].describe().to_dict()

        # Trend detection (simple)
        trends = {}
        for col in numeric_cols:
            if df[col].iloc[-1] > df[col].iloc[0]:
                trends[col] = "increasing 📈"
            elif df[col].iloc[-1] < df[col].iloc[0]:
                trends[col] = "decreasing 📉"
            else:
                trends[col] = "stable ➖"

        summary["trends"] = trends

    # Categorical analysis
    categorical_cols = df.select_dtypes(exclude="number").columns

    if len(categorical_cols) > 0:
        category_summary = {}
        for col in categorical_cols:
            category_summary[col] = df[col].value_counts().head(5).to_dict()

        summary["top_categories"] = category_summary

    return df, summary