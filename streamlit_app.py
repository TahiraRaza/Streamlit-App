
import streamlit as st
from PIL import Image

# Function to format numbers with spaces
def format_sek(amount):
    # Manually format SEK using spaces instead of commas
    return f"{amount:,.0f}".replace(",", " ")

# Title of the app
st.title("House Price and Loan Calculator")

# Display the image
# image = Image.open(r"D:/HV-filesync/tara0001/Desktop/Data Scientist/Machine learning/Kunskapskontroll_2/Kunskapskontroll_2_Tahira_Raza_ny/Streamlit/sunset_1.png")
image = Image.open("sunset_1.png")
image = image.resize((600, 400))  # Resize to desired width and height
st.image(image, use_container_width=True)

# 1. Calculate 15% of the entered house price
st.header("Down Payment Calculation")

house_price = st.number_input("Enter House Price (in SEK):", min_value=0)

if house_price > 0:
    house_price_15_percent = house_price * 0.15
    formatted_house_price = format_sek(house_price)
    formatted_house_price_15_percent = format_sek(house_price_15_percent)
    st.write(f"15% of {formatted_house_price} SEK is: {formatted_house_price_15_percent} SEK")

# 2. Loan Calculator - Monthly amortization and interest
st.header("Loan Amortization and Interest Calculator")

loan_amount = st.number_input("Enter Loan Amount (in SEK):", min_value=0)
loan_years = st.number_input("Enter Number of Years to Repay the Loan:", min_value=1)

# Interest rate input by the user
interest_rate = st.number_input("Enter Annual Interest Rate (in %):", min_value=0.0, step=0.01) / 100  # convert percentage to decimal

if loan_amount > 0 and loan_years > 0 and interest_rate > 0:
    # Calculate monthly interest rate
    monthly_interest_rate = interest_rate / 12
    
    # Calculate number of months
    months = loan_years * 12
    
    # Calculate monthly amortization using the formula
    monthly_payment = (loan_amount * monthly_interest_rate) / (1 - (1 + monthly_interest_rate) ** -months)
    
    # Calculate total interest
    total_interest = monthly_payment * months - loan_amount
    
    formatted_monthly_payment = format_sek(monthly_payment)
    formatted_total_interest = format_sek(total_interest)
    
    st.write(f"Monthly Payment: {formatted_monthly_payment} SEK")
    st.write(f"Total Interest Paid: {formatted_total_interest} SEK")


