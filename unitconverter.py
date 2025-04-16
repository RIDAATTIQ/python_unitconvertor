import streamlit as st  # Streamlit ko import karna

def km_to_miles(km):
    return km * 0.621371

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# Streamlit title aur explanation
st.title("Unit Converter 💫")
st.write("Welcome to the Unit Converter! Choose the conversion type below:")

# Options for conversion
choice = st.radio("Select conversion type", ("Kilometers to Miles", "Celsius to Fahrenheit"))

if choice == "Kilometers to Miles":
    km = st.number_input("Enter distance in kilometers", min_value=0.0)
    if km:
        miles = km_to_miles(km)
        st.write(f"{km} km is equal to {miles} miles")

elif choice == "Celsius to Fahrenheit":
    celsius = st.number_input("Enter temperature in Celsius", min_value=-273.15)
    if celsius:
        fahrenheit = celsius_to_fahrenheit(celsius)
        st.write(f"{celsius}°C is equal to {fahrenheit}°F")
