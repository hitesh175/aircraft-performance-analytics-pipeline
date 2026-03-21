import sqlite3
import pandas as pd

def create_feature_table():

    conn = sqlite3.connect("database/aircraft.db")

    query = """

    SELECT
        Company,
        Engine_Type,
        SHP,
        AUW,
        Vcruise,
        Vmax,
        ROC,
        Range,
        Aircraft_Type,

        (Vmax - Vcruise) AS speed_gap,
        (SHP * 1.0 / AUW) AS power_to_weight

    FROM aircraft_data

    WHERE Range IS NOT NULL

    """

    df = pd.read_sql_query(query, conn)

    conn.close()

    print("Feature table created")

    return df