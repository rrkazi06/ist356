import streamlit as st
import pandas as pd
import numpy as np

# url = "https://raw.githubusercontent.com/mafudge/datasets/refs/heads/master/delimited/students-header.psv" # psv is pipe separated value

# data = pd.read_csv(url, sep="|")
# st.dataframe(data) # prints a nice looking data frame

# let's try the file w/ no header/metadata

# url = "https://raw.githubusercontent.com/mafudge/datasets/refs/heads/master/delimited/students-no-header.csv"

# data = pd.read_csv(url, header=None, names=["Name", "Grade", "Year"]) # without the header thing, it makes the first row the headers. without names, it'll just use arbitrary numbers

# st.dataframe(data) 

url = "https://raw.githubusercontent.com/mafudge/datasets/refs/heads/master/delimited/students-header-blanks.csv"

data = pd.read_csv(url, skiprows=5)
st.dataframe(data)
