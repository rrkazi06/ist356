import streamlit as st
from figures import *

# output = df4['AMT'].str\
#     .replace('$','').str.replace(',','').astype

# st.write(output)

# output = pd.merge(df1, df2, how='inner', left_on='COLB', right_on='COLD')
output2= df8.pivot(index='COLA', columns='COLB', values='COLC')
st.write(output2)

#one column in a data frame = series

