import datetime as dt
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st
import seaborn as sns

data = sns.load_dataset("dowjones")


def main():
    st.write("test")
    st.dataframe(data)
    st.write(sns.get_dataset_names())


if __name__ == "__main__":
    main()
