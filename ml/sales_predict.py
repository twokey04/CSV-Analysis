from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import pandas as pd


class SalesPredictor:
    def __init__(self, merged_df):
        self.merged_df = merged_df
        self.model = None

    def prepare_data_for_ml(self):
        """Prepare data for machine learning."""
        df = self.merged_df[['Sales', 'CostPrice']]
        return df

    def train_model(self):
        """Train a linear regression model."""
        df = self.prepare_data_for_ml()
        X = df[['CostPrice']]
        y = df['Sales']
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        self.model = LinearRegression()
        self.model.fit(X_train, y_train)

        y_pred = self.model.predict(X_test)
        mse = mean_squared_error(y_test, y_pred)
        r2 = r2_score(y_test, y_pred)
        print(f"Mean Squared Error (MSE): {mse}")
        print(f"R-squared (R2): {r2}")

    def predict_future_sales(self, future_data):
        """Predict future sales based on the trained model."""
        if self.model is None:
            raise ValueError("Model has not been trained.")
        future_df = pd.DataFrame(future_data, columns=['CostPrice'])
        future_df['PredictedSales'] = self.model.predict(future_df)
        return future_df
