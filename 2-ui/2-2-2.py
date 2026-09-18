import streamlit as st

st.title("Order Tracker")

# Initialize variables

if 'total' not in st.session_state:
    st.session_state.total = 0
    st.session_state.history = []

# Inputs
amount = st.number_input("Order Amount:")
total_button = st.button("Calculate Total", type="primary")
clear_button = st.button("Clear")

# Process (avoid outputting, just manipulate data)
if total_button:
    st.session_state.total += amount # x = x+1 <=> x+=1
    st.session_state.history.append(amount)

if clear_button:
    st.session_state.total = 0
    st.session_state.history = []

# Outputs
st.write(f"Total Order: {st.session_state.total}")
st.write(f"History: {st.session_state.history}")