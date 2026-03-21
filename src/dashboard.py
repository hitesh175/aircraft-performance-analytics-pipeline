import streamlit as st
import pandas as pd
from sqlalchemy import create_engine
import joblib
import plotly.express as px
from streamlit_autorefresh import st_autorefresh

# Page setup
st.set_page_config(layout="wide")

# Auto refresh every 10 seconds
st_autorefresh(interval=10000, key="datarefresh")

# Database connection
engine = create_engine(
"mysql+pymysql://aircraft_user:aircraft123@localhost:3306/aircraft_db"
)

# Title
st.title("Aircraft Performance Analytics Dashboard")

# Load data
df = pd.read_sql("SELECT * FROM aircraft_data", engine)


st.sidebar.header("Filters")

aircraft_type = st.sidebar.selectbox(
    "Aircraft Type",
    ["All"] + sorted(df["aircraft_type"].dropna().unique())
)

company = st.sidebar.selectbox(
    "Company",
    ["All"] + sorted(df["company"].dropna().unique())
)

engine_type = st.sidebar.selectbox(
    "Engine Type",
    ["All"] + sorted(df["engine_type"].dropna().unique())
)

filtered_df = df.copy()

if aircraft_type != "All":
    filtered_df = filtered_df[filtered_df["aircraft_type"] == aircraft_type]

if company != "All":
    filtered_df = filtered_df[filtered_df["company"] == company]

if engine_type != "All":
    filtered_df = filtered_df[filtered_df["engine_type"] == engine_type]



st.header("Dataset Overview")

col1, col2, col3 = st.columns(3)

col1.metric("Total Aircraft", len(filtered_df))
col2.metric("Average Range", round(filtered_df["range_value"].mean(),2))
col3.metric("Average Cruise Speed", round(filtered_df["vcruise"].mean(),2))

st.divider()



st.subheader("Dataset Preview")

st.write(
"This table shows a preview of the aircraft dataset retrieved from the MySQL database."
)

st.dataframe(
filtered_df.head(1000),
width="stretch",
height=400
)


# DOWNLOAD DATASET
st.subheader("Download Filtered Dataset")

csv = filtered_df.to_csv(index=False).encode("utf-8")

st.download_button(
"Download Dataset as CSV",
csv,
"aircraft_filtered_dataset.csv",
"csv"
)

st.divider()

# OBJECTIVE 1
st.subheader("Objective 1: Aircraft Type Distribution")

fig1 = px.pie(
filtered_df,
names="aircraft_type",
title="Aircraft Type Distribution",
hole=0.4
)

st.plotly_chart(fig1, width="stretch")

st.divider()

# OBJECTIVE 2
st.subheader("Objective 2: Aircraft with Highest Range")

top10 = filtered_df.sort_values(
"range_value",
ascending=False
).head(10)

fig2 = px.bar(
top10,
x="company",
y="range_value",
title="Top Aircraft by Range",
color="range_value"
)

st.plotly_chart(fig2, width="stretch")

st.divider()

# OBJECTIVE 3
st.subheader("Objective 3: Cruise Speed vs Range")

fig3 = px.scatter(
filtered_df,
x="vcruise",
y="range_value",
color="aircraft_type",
hover_data=["company","engine_type"],
title="Cruise Speed vs Range"
)

st.plotly_chart(fig3, width="stretch")

st.divider()

# OBJECTIVE 4
st.subheader("Objective 4: Engine Type Performance")

engine_perf = (
filtered_df
.groupby("engine_type")["range_value"]
.mean()
.reset_index()
)

fig4 = px.bar(
engine_perf,
x="engine_type",
y="range_value",
title="Average Range by Engine Type",
color="engine_type"
)

st.plotly_chart(fig4, width="stretch")

st.divider()

# OBJECTIVE 5
st.header("Objective 5: Predict Aircraft Range Using Machine Learning")

model = joblib.load("aircraft_model.pkl")

col1, col2 = st.columns(2)

with col1:

    shp = st.slider(
        "Engine Power (SHP)",
        int(df["shp"].min()),
        int(df["shp"].max()),
        int(df["shp"].mean())
    )

    auw = st.slider(
        "Aircraft Weight (AUW)",
        int(df["auw"].min()),
        int(df["auw"].max()),
        int(df["auw"].mean())
    )

    vcruise = st.slider(
        "Cruise Speed",
        int(df["vcruise"].min()),
        int(df["vcruise"].max()),
        int(df["vcruise"].mean())
    )

with col2:

    vmax = st.slider(
        "Maximum Speed",
        int(df["vmax"].min()),
        int(df["vmax"].max()),
        int(df["vmax"].mean())
    )

    roc = st.slider(
        "Rate of Climb",
        int(df["roc"].min()),
        int(df["roc"].max()),
        int(df["roc"].mean())
    )

if st.button("Predict Aircraft Range"):

    input_data = pd.DataFrame({
        "shp":[shp],
        "auw":[auw],
        "vcruise":[vcruise],
        "vmax":[vmax],
        "roc":[roc]
    })

    prediction = model.predict(input_data)[0]

    st.success(f"Predicted Aircraft Range: {round(prediction,2)}")