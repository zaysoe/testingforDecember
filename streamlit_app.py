import streamlit as st

## input_data = input("Enter a number")
number = st.number_input('Insert a number')
st.write('The current number is ', number)

st.write(10*number)

options = st.multiselect(
    'What are your favorite colors',
    ['Green', 'Yellow', 'Red', 'Blue'],
    ['Yellow', 'Red'])

st.write('You selected:', options)