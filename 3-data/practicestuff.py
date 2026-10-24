import streamlit as st
import pandas as pd
import numpy as np

gpas = pd.Series([4.0, np.nan, 3.4, 2.8, 2.5], index=['Allen','Bob','Chris','Ed','Frank'])
yrs  = pd.Series(['So','Fr','Jr','Sr'],       index=['Allen','Bob','Dave','Frank'])
pd.DataFrame({'GPA': gpas, 'Year': yrs})


