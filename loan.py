#LOAN CALCULATOR

#ALGORITHM
#Import necessary functions and libraries
#Welcome the user to system
#Ask user if they have a total principal or monthly payment amount to input
#Ask the user for terms of loan: principal/payment, interest rate, years
#Calculate the principal/payment not provided by the user
#Ask user if they want the amortization schedule/graph
#Create payment schedule with monthly balances
#Create comparison graph and output to screen
#Ask user if they wish to export the schedule
#Create CSV of amortization schedule


#IMPORT LIBRARIES AND FUNCTIONS
from datetime import date, datetime #date validation
import pandas as pd #used to help covert to csv
import matplotlib.stackplot as splt #display graph of payments over time

from loan_calc_functions import * #import custom functions

user_prin = 0.00
user_pmt = 0.00
user_irate = 0.01
user_term = 1
user_start = date(2026,1,1)

print("Welcome to the loan calculator. Pleaase be prepared to enter principal/payment, interest rate, term, and start date.")
reqvalidation() #requests and validates data from user