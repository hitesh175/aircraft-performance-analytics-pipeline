import pandas as pd
from sqlalchemy import create_engine

# MySQL connection
engine = create_engine(
    "mysql+pymysql://aircraft_user:aircraft123@localhost:3306/aircraft_db"
)

def load_data():

    # LOAD DATASETS
    airplane = pd.read_csv("data/Airplane_Complete_Imputation.csv")
    helicopter = pd.read_csv("data/Helicopter_BlueBook.csv")

    # clean column names
    airplane.columns = airplane.columns.str.strip()
    helicopter.columns = helicopter.columns.str.strip()

    # AIRPLANE DATA CLEANING
    airplane = airplane.rename(columns={
        "Company": "company",
        "Engine Type": "engine_type",
        "Engine_Type": "engine_type",
        "SHP": "shp",
        "AUW": "auw",
        "Vcruise": "vcruise",
        "Vmax": "vmax",
        "ROC": "roc",
        "Range": "range_value"
    })

    airplane["aircraft_type"] = "Airplane"

    airplane = airplane[
        [
            "company",
            "engine_type",
            "shp",
            "auw",
            "vcruise",
            "vmax",
            "roc",
            "range_value",
            "aircraft_type"
        ]
    ]

    # HELICOPTER DATA CLEANING
    helicopter = helicopter.rename(columns={
        "Company": "company"
    })

    if "engine_type" not in helicopter.columns:
        helicopter["engine_type"] = None

    # helicopters don't have these values
    helicopter["shp"] = None
    helicopter["auw"] = None

    helicopter["aircraft_type"] = "Helicopter"

    helicopter = helicopter[
        [
            "company",
            "engine_type",
            "shp",
            "auw",
            "vcruise",
            "vmax",
            "roc",
            "range_value",
            "aircraft_type"
        ]
    ]

    # MERGE DATASETS
    df = pd.concat([airplane, helicopter], ignore_index=True)

    # convert numeric columns
    numeric_cols = ["shp","auw","vcruise","vmax","roc","range_value"]

    for col in numeric_cols:
        df[col] = pd.to_numeric(df[col], errors="coerce")

    # LOAD INTO MYSQL
    df.to_sql(
        "aircraft_data",
        engine,
        if_exists="replace",
        index=False
    )

    print("Data loaded successfully into MySQL")

    # EXPORT DATABASE TO FINAL CSV
    final_df = pd.read_sql("SELECT * FROM aircraft_data", engine)

    final_df.to_csv(
        "data/final_aircraft_dataset.csv",
        index=False
    )

    print("Final CSV exported from MySQL database")