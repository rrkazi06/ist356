import streamlit as st

st.title("Area and Perimeter Calculator")

length = st.number_input("Enter the length of the rectangle:", min_value=0.0, max_value=1000.0, value=1.0)
width = st.number_input("Enter the width of the rectangle:", min_value=0.0, max_value=1000.0, value=1.0)

area = length * width
perimeter = 2 * (length + width)

button_1 = st.button("Calculate Area")
button_2 = st.button("Calculate Perimeter")
clear_button = st.button("Clear")

if button_1:
    st.write(f"Area of Rectangle: {area}")
if button_2:
    st.write(f"Perimeter of Rectangle: {perimeter}")
if clear_button:
    st.write("Inputs cleared.")