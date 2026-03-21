
# Project Title

A brief description of what this project does and who it's for

Note: Please Install All the Module Requirements before Running The Code.

---

# Aircraft Performance Analytics Pipeline

## Project Overview

This project implements a **data engineering and analytics pipeline** for analyzing aircraft performance data.
The system integrates multiple aviation datasets, stores them in a relational database, and provides insights through an **interactive dashboard and machine learning model**.

The pipeline processes aircraft data, stores it in a **MySQL data warehouse**, and enables users to explore aircraft performance metrics such as **range, cruise speed, engine type, and manufacturer comparisons**.

Additionally, a **machine learning model predicts aircraft operational range based on key performance parameters**.

---

# Project Architecture

The project follows a typical **ETL (Extract–Transform–Load) data pipeline architecture**.

```
CSV Airplane Dataset

CSV Helicopter Dataset
        ↓
Extract (Python – Pandas)
        ↓
Transform (Data Cleaning + Standardization)
        ↓
Load (MySQL Database)
        ↓
Machine Learning Model
        ↓
Interactive Dashboard (Streamlit)
```

---

# Objectives

The main objectives of this project are:

### 1. Data Integration

Combine airplane and helicopter datasets into a **single unified dataset**.

### 2. Data Storage

Store structured aircraft performance data in a **MySQL relational database**.

### 3. Data Analysis

Analyze aircraft performance metrics such as:

* Operational range
* Cruise speed
* Engine performance
* Aircraft manufacturer distribution

### 4. Machine Learning Prediction

Build a regression model that **predicts aircraft range based on performance features**.

### 5. Interactive Visualization

Provide a **Streamlit dashboard** that allows users to explore aircraft data and compare aircraft characteristics interactively.

---

# Technologies Used

| Technology   | Purpose                            |
| ------------ | ---------------------------------- |
| Python       | Data pipeline and machine learning |
| Pandas       | Data extraction and transformation |
| MySQL        | Data warehouse                     |
| SQLAlchemy   | Python–MySQL connection            |
| Scikit-learn | Machine learning model             |
| Streamlit    | Interactive dashboard              |
| Plotly       | Interactive charts                 |
| Joblib       | Model serialization                |

---

# Project Structure

```
aircraft_pipeline
│
├── data
│   ├── Airplane_Complete_Imputation.csv
│   └── Helicopter_BlueBook.csv
│
├── src
│   ├── load_to_mysql.py
│   ├── train_model.py
│   └── dashboard.py
│
├── run_pipeline.py
├── requirements.txt
└── README.md
```

---

# Database Schema

The database stores aircraft performance information in the table:

### aircraft_data

| Column        | Description                               |
| ------------- | ----------------------------------------- |
| company       | Aircraft manufacturer                     |
| engine_type   | Type of engine                            |
| shp           | Engine power                              |
| auw           | Aircraft weight                           |
| vcruise       | Cruise speed                              |
| vmax          | Maximum speed                             |
| roc           | Rate of climb                             |
| range_value   | Operational range                         |
| aircraft_type | Aircraft category (Airplane / Helicopter) |

---

# ETL Pipeline

The ETL pipeline performs the following steps:

### Extract

Aircraft data is extracted from two CSV datasets:

* Airplane dataset
* Helicopter dataset

### Transform

The transformation step includes:

* Cleaning column names
* Standardizing schema
* Handling missing values
* Merging both datasets

### Load

The processed dataset is loaded into the **MySQL database** using SQLAlchemy.

---

# Machine Learning Model

A **Random Forest Regressor** is used to predict aircraft operational range.

### Input Features

* Engine Power (SHP)
* Aircraft Weight (AUW)
* Cruise Speed
* Maximum Speed
* Rate of Climb

The trained model is saved as:

```
aircraft_model.pkl
```

This model is used by the dashboard to generate real-time predictions.

---

# Installation

Install required libraries:

```bash
pip install -r requirements.txt
```

---

# Database Setup

Run the following SQL commands in MySQL Workbench:

```sql
CREATE DATABASE aircraft_db;

USE aircraft_db;

CREATE TABLE aircraft_data (
    company VARCHAR(100),
    engine_type VARCHAR(100),
    shp FLOAT,
    auw FLOAT,
    vcruise FLOAT,
    vmax FLOAT,
    roc FLOAT,
    range_value FLOAT,
    aircraft_type VARCHAR(50)
);
```

Create a database user:

```sql
CREATE USER 'aircraft_user'@'localhost' IDENTIFIED BY 'aircraft123';

GRANT ALL PRIVILEGES ON aircraft_db.* TO 'aircraft_user'@'localhost';

FLUSH PRIVILEGES;
```

---

# Running the Data Pipeline

Run the pipeline to load data and train the model:

```bash
python run_pipeline.py
```

This script will:

1. Load the datasets
2. Clean and merge the data
3. Insert data into MySQL
4. Train the machine learning model

---

# Running the Dashboard

Launch the dashboard:

```bash
python -m streamlit run src/dashboard.py
```

Open in your browser:

```
http://localhost:8501
```

---

# Dashboard Features

The dashboard provides:

* Aircraft performance analysis
* Manufacturer comparison
* Engine type performance visualization
* Cruise speed vs range analysis
* Top aircraft by operational range
* Aircraft type filtering
* Interactive charts
* Aircraft range prediction tool

---

# Example Use Case

Users can simulate a new aircraft configuration by adjusting parameters such as:

* Engine power
* Aircraft weight
* Cruise speed
* Maximum speed
* Rate of climb

The dashboard predicts the **expected operational range** using the trained machine learning model.

---

# Future Improvements

Possible extensions include:

* Adding additional aviation datasets
* Implementing automated data pipelines with Airflow
* Deploying the dashboard to the cloud
* Using advanced machine learning models

---

# Author

Hitesh Kanagala Rajendra Prasad

---

