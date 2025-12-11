#LOAN CALCULATOR

#ALGORITHM
#Import necessary functions and libraries
#Welcome the user to system and tell them which inputs are required
#Ask user if they have a total principal or monthly payment amount to input
#Ask the user for terms of loan and validate: principal/payment, interest rate, years
#Calculate the principal/payment not provided by the user
#Create payment schedule with monthly balances
#Create comparison graph and output to screen
#Export amortization schedule to CSV file

#IMPORT LIBRARIES AND FUNCTIONS
from datetime import date, datetime #date validation
from loan_calc_functions import * #import custom functions

#NEEDS TO BE ***MANUALLY*** INSTALLED PRIOR TO RUNNING
import pandas as pd #used to help covert to csv, (pip install pandas)
#import matplotlib.stackplot as splt #display graph of payments over time (pip install matplotlib) 

user_prin = 0.00
user_pmt = 0.00
user_irate = 0.01
user_term = 1
user_start = date(2026,1,1)

print("Welcome to the loan calculator. Pleaase be prepared to enter principal/payment, interest rate, term, and first payment due date.")
reqvalidation() #requests and validates data from user