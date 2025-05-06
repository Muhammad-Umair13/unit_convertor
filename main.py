import streamlit as st

st.title(" 🔄 Unit Convertor")

selection = st.selectbox("Select convertor", ["Length", "Mass", "Temperature"])

if selection == "Length":
    col1,col2 = st.columns(2)
    with col1:
        st.header("Meter")
        num = st.number_input("Enter Number: ", min_value=0)
        cal = num * 100
    with col2:
        st.header("Centimeter")
        st.header(cal)


elif selection == "Mass":
    col1,col2 = st.columns(2)
    with col1:
        st.header("Kilogram")
        num = st.number_input("Enter Number: ", min_value=0)
        cal = num * 1000
    with col2:
        st.header("Gram")
        st.header(cal)


elif selection == "Temperature":
    col1,col2 = st.columns(2)
    with col1:
        st.header("Celsius")
        num = st.number_input("Enter Number: ", min_value=0)
        cal = (num * 9/5) + 32
    with col2:
        st.header("Fahrenheit")
        st.header(cal)