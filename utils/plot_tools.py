import datetime as dt
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import seaborn as sns


def generate_data():
    df = sns.load_dataset("dowjones")
    return df


def generate_extracted_dataframe(df: pd.DataFrame, start_dt: dt.date, end_dt: dt.date):
    return df
