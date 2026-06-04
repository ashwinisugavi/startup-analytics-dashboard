import pandas as pd
import streamlit as st

@st.cache_data
def load_data():

    df = pd.read_csv("startup_data.csv")

    # Remove duplicates
    df.drop_duplicates(inplace=True)

    # Fill missing values
    numeric_cols = df.select_dtypes(include=['number']).columns

    for col in numeric_cols:
        df[col].fillna(df[col].median(), inplace=True)

    return df


def get_numeric_columns(df):
    return df.select_dtypes(include=['number']).columns.tolist()


def get_categorical_columns(df):
    return df.select_dtypes(include=['object']).columns.tolist()
