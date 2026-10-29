# Aircraft Performance Analytics Pipeline

A Python analytics project combining aircraft CSV preparation, MySQL storage, Random Forest range prediction, and a Streamlit dashboard.

## Workflow

```text
Aircraft CSVs → Pandas transformations → MySQL
                                          ├─ Random Forest model
                                          └─ Streamlit analytics
```

## Repository guide

| Path | Purpose |
| --- | --- |
| [Data](Data/) | Source, imputed, and exported CSVs |
| [src/load_to_mysql.py](src/load_to_mysql.py) | Cleaning, merging, database replacement, CSV export |
| [src/sql_transform.py](src/sql_transform.py) | SQL transformation |
| [src/train_model.py](src/train_model.py) | Model training and R² reporting |
| [src/dashboard.py](src/dashboard.py) | Interactive dashboard |
| [database](database/) | SQL and database diagram material |
| [outputs](outputs/) | Saved charts and screenshots |
| [run_pipeline.py](run_pipeline.py) | Pipeline entry point |

![Dashboard preview](outputs/Dashboard%20Data%20Preview.png)

## Setup and execution

Create a Python virtual environment and install:

```bash
python -m pip install -r requirements.txt
```

Before running, prepare a local MySQL `aircraft_db` database and configure the connection strings used by the source files.

Two source-level setup issues need attention:

- The repository directory is `Data/`, while the loader references `data/`. Align these paths on case-sensitive systems.
- Database connection details are hard-coded. Replace them with your local configuration and avoid committing real credentials.

Then run from the repository root:

```bash
python run_pipeline.py
python -m streamlit run src/dashboard.py
```

The loader replaces the `aircraft_data` table. Use a dedicated project database.

## Model and limitations

The regressor predicts `range_value` from `shp`, `auw`, `vcruise`, `vmax`, and `roc`. Training drops rows with missing values, uses an 80/20 random split, prints R², and saves `aircraft_model.pkl`.

Helicopter rows receive missing power/weight values in the loader and may therefore be excluded from training. The forest has no fixed random seed, so scores can vary. Existing model files and screenshots are saved artifacts; they are not a freshly reproduced benchmark or an aviation planning tool.
