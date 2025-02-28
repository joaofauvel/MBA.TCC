# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.16.7
#   kernelspec:
#     display_name: MBA.TCC
#     language: python
#     name: mba.tcc
# ---

# %%
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.compose import make_column_selector, make_column_transformer, ColumnTransformer
from sklearn.pipeline import make_pipeline, make_union, Pipeline, FeatureUnion

# %% language="sh"
# ls ../data

# %%
import os
os.listdir("../data")

# %%
data = (
    pd.read_csv(
        "../data/ILHA_SOLTEIRA.csv", 
        decimal=".", 
        delimiter=",",
    )
    .assign(
        Date=lambda df: pd.to_datetime(df.Date, errors="raise", format="%d-%m-%Y"),
    )
    .set_index("Date")
    .reindex()
)
data

# %%
data.describe()

# %%
data.isna().sum().sort_values(ascending=False)

# %%
