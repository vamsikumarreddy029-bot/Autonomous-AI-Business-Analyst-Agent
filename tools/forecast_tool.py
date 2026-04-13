import numpy as np
from sklearn.linear_model import LinearRegression


def forecast(df):
    numeric_cols = df.select_dtypes(include="number").columns

    # ❌ No numeric data
    if len(numeric_cols) == 0:
        return {
            "error": "No numeric columns available for forecasting"
        }

    results = {}

    for col in numeric_cols:
        try:
            y = df[col].dropna().values

            # Need enough data
            if len(y) < 3:
                results[col] = "Not enough data"
                continue

            # Create X (time index)
            X = np.arange(len(y)).reshape(-1, 1)

            # Train model
            model = LinearRegression()
            model.fit(X, y)

            # Predict next 3 points
            future_X = np.arange(len(y), len(y) + 3).reshape(-1, 1)
            predictions = model.predict(future_X)

            results[col] = {
                "next_3_predictions": predictions.tolist(),
                "trend": (
                    "increasing 📈"
                    if predictions[-1] > y[-1]
                    else "decreasing 📉"
                )
            }

        except Exception as e:
            results[col] = f"Error: {str(e)}"

    return results