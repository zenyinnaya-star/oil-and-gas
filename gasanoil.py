welcome='Welcome to Gas and Oil Data Analysis Tool'
description='This tool provides functionalities to analyze and visualize gas and oil data.'
author='Data Analysis Team'
version='1.0.0'
license='MIT License'
print("-" * 50)
print(welcome)
print(description)
print(f"Author: {author}")
print(f"Version: {version}")
print(f"License: {license}")
print("-" * 50)
# This is a placeholder for the actual gas and oil data analysis functionalities.
print(" select purchace type: ")
selection_gas=" G: Gas"
selection_oil=" O: Oil"
print(selection_gas)
print(selection_oil)
# normalize choice to accept G/g and O/o
user_choice = input("Please select an option (G/O): ").strip().lower()
# get province input
province = input("Enter the province (e.g., ON, QC, BC): ").strip().upper()
# initialize variables
gst_rate = 0
total_cost=0
gas_price=0 
gas_disprice=0

if user_choice == 'G' or user_choice == 'g':
    number_of_gas_liters=int(input("Enter the number of gas liters: "))
    if number_of_gas_liters > 4000:
        gas_disprice = number_of_gas_liters * 1.07 * 0.9
        total_liter_cost = gas_disprice
        total_cost = total_liter_cost
    else:
        # non-discounted gas price: $1.07 per litre (no *12)
        gas_price = number_of_gas_liters * 1.07
        total_liter_cost = gas_price
        total_cost = total_liter_cost
elif user_choice == 'O' or user_choice == 'o':    
    number_of_oil_liters=int(input("Enter the number of oil cases: "))
    if number_of_oil_liters > 8:
        oil_disprice = number_of_oil_liters * 1.27 * 0.90 * 12
        total_case_cost = oil_disprice
        total_cost = total_case_cost
    else:
        oil_price = number_of_oil_liters * 1.27 * 12
        total_case_cost = oil_price
        total_cost = total_case_cost
else:
    print("Invalid option selected. Please choose either 'G' for Gas or 'O' for Oil.") 

# gst_rate stored as multiplier: e.g. 1.13 means +13%
if province == "ON":
    gst_rate = 1.13
elif province == "OTHER":
    gst_rate = 1.15
else:
    gst_rate = 1.05

# compute GST amount and final total
gst_amount = total_cost * (gst_rate - 1)
final_amount = total_cost * gst_rate
print("-" * 50)
if user_choice == 'G' or user_choice == 'g':
    print(f'product type: Gas')
    print(f"Number of liters: {number_of_gas_liters} ")
    print(f"Price before/: ${gas_price:.2f}")
    print(f"Price after discount : ${total_liter_cost:.2f}")
    print(f"GST: ${gst_amount:.2f}")
    print(f"The final amount for gas purchase in {province} is: ${final_amount:.2f}")
elif user_choice == 'O' or user_choice == 'o':
    print(f'product type: Oil')
    print(f"Number of cases: {number_of_oil_liters} ")
    print(f'price before discount: ${total_case_cost:.2f}')
    print(f"GST: ${gst_amount:.2f}")
    print(f"The final amount for oil purchase in {province} is: ${final_amount:.2f}")
print("-" * 50)
print("Thank you for using the Gas and Oil Data Analysis Tool!")