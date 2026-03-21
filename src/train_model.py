import pandas as pd
from sqlalchemy import create_engine
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score
import joblib

# MySQL connection
engine = create_engine(
"mysql+pymysql://aircraft_user:aircraft123@localhost:3306/aircraft_db"
)

def train_model():

    # Load data from MySQL
    df = pd.read_sql("SELECT * FROM aircraft_data", engine)

    # Remove missing values
    df = df.dropna()

    # Use ONLY numeric features for prediction
    features = ["shp","auw","vcruise","vmax","roc"]

    X = df[features]
    y = df["range_value"]

    # Split dataset
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42
    )

    # Train model
    model = RandomForestRegressor()

    model.fit(X_train, y_train)

    # Test predictions
    predictions = model.predict(X_test)

    score = r2_score(y_test, predictions)

    print("Model R2 Score:", score)

    # Save model
    joblib.dump(model, "aircraft_model.pkl")

    print("Model saved successfully")