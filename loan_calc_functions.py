#CREATE FUNCTIONS FOR MAIN

#IMPORT FUNCTION LIBRARIES
from datetime import date, datetime
import pandas as pd
import matplotlib.stackplot as splt

#PRINCIPAL VERIFICATION
def principalv(): #while loop to check principal amount, returns user_prin
    iscontinued = True
    while iscontinued == True:
        user_prin = input("How much is the principal of your loan? ")
        try: #test if user entered numeric value
            user_prin = float(user_prin)
        except ValueError:
            print("Try entering a number instead of a string.")  
        else: #covert to float and test if within upper and lower bounds
            user_prin = float(user_prin)   
            if user_prin < 500.00:
                print("Are you sure you need a micro loan? Why don't you try saving up some money for this purchase :)")    
            elif user_prin >= 10000000.00:
                print("Whoa there Mr. Moneybags! Why don't you consult your personal wealth manager with this one. ")
            else: #continues until a numeric value within bounds is entered 
                iscontinued = False 
    return(user_prin)
  
#PAYMENT VERIFICATION
def paymentsv(): #while lopp to check payment anount, returns user_pmt
    iscontinued = True
    while iscontinued == True:
        user_pmt = input("How much is the payment of your loan? Please use whole numbers. ")
        try: #test if user entered numeric value
            user_pmt = float(user_pmt)
        except ValueError:
            print("Try entering a number instead of a string.")
        else: #covert to float and test if within upper and lower bounds
            user_pmt = float(user_pmt)
            if user_pmt < 50.00:
                print("Are you sure you need a micro loan? Why don't you try saving up some money for this purchase :)")    
            elif user_pmt >= 100000.00:
                print("Whoa there Mr. Moneybags! Why don't you consult your personal wealth manager with this one. ")
            else: #continues until a numeric value within bounds is entered 
                iscontinued = False  
    return(user_pmt)

#INTEREST VERIFICATION
def interestv(): #whiel loop to check the interest rate, returns user_irate
    iscontinued = True
    while iscontinued == True:
        user_irate = input("How much is the interest rate per year? Enter as a decimal, not a percent. ")
        try: #test if user entered numeric value
            user_irate = float(user_irate)
        except ValueError:
            print("Try entering a number instead of a string.")
        else: #covert to float and test if within upper and lower bounds
            user_irate = float(user_irate)   
            if user_irate < 0.01:
                print("Did grandma give you this loan? Try using an interest rate greater than or equal to 0.01.")    
            elif user_irate > 0.30:
                print("What is this, a payday loan? Usuary is a crime. Know your rights.")
            else: #continues until a numeric value within bounds is entered 
                iscontinued = False  
    return(user_irate)

#TERM VERIFICATION
def termv(): #while loop to check term length, returns user_term
    iscontinued = True
    while iscontinued == True:
        user_term = input("What is the term of your loan in years? ")
        try: #test if user entered numeric value
            user_term = int(user_term)
        except ValueError:
            print("Try entering a whole number instead of a string or decimals.")
        else: #covert to integar and test if within upper and lower bounds
            user_term = int(user_term)
            if user_term < 1:
                print("Please try using a term of 1 year or greater.")    
            elif user_term > 40:
                print("What kind of dystopian loan term is this? Try using a term of 40 years or less.")
            else: #continues until a numeric value within bounds is entered 
                iscontinued = False   
    return(user_term)

#DATE VERIFICATION
def datev(): #while loop to check the start date, returns user_start
    iscontinued = True
    while iscontinued == True:
        user_date = input("Please enter the loan start date as YYYY-MM-DD: ")
        #if stmt for null = today
        if user_date == "":
            user_start = date.today()
            iscontinued = False
        else:
            try: #test if user entered date value
                user_start = datetime.strptime(user_date, "%Y-%m-%d").date()
            except ValueError:
                print("Invalid date format. Please enter a valid date in YYYY-MM-DD format")   
            else: #continues until a date value is entered 
                iscontinued = False
    return user_start

#CALCULATE PAYMENT FROM USER PRINCIPAL
def paymentc(user_prin, user_irate, user_term): #calculate a payment amount from user inputs, returns user_pmt

    user_pmt = user_prin * ((user_irate/12)*pow((1+(user_irate/12)), user_term*12) / (pow((1+(user_irate/12)), user_term*12)-1))

    return(user_pmt)

#CALCULATE PRINCIPAL FROM USER PAYMENT
def principalc(user_pmt, user_irate, user_term): #calculate a principal amount from user inputs, returns user_prin

    user_prin = user_pmt / ((user_irate/12)*pow((1+(user_irate/12)), user_term*12) / (pow((1+(user_irate/12)), user_term*12)-1))

    return(user_prin)

#DATA REQUEST AND VALIDATION
def reqvalidation(): #loop to determine payment calculation required and necessary inputs, displays user responses and calculations to screen
    global user_prin
    global user_pmt
    global user_irate
    global user_term

    iscontinued = True
    while iscontinued == True:
        calctype = input("Would you like to start with the principal[1] or payment[2] amount, or would you like to exit[3]? ")
        try: #test if user entered numeric value
            calctype = int(calctype)
        except ValueError:
            print("Try entering a whole number instead of a string or decimals.")
        else: #covert to integar and test if within upper and lower bounds
            calctype = int(calctype)  
            if calctype > 3 or calctype < 1:
                print("Try entering one of the options in [brackets].")
            elif calctype == 1:
                user_prin = principalv()
                user_irate = interestv()
                user_term = termv()
                user_pmt = paymentc(user_prin, user_irate, user_term)
                user_date = datev()
                iscontinued = False
            elif calctype == 2:
                user_pmt = paymentsv()
                user_irate = interestv()
                user_term = termv()
                user_prin = principalc(user_pmt, user_irate, user_term)
                user_date = datev()
                iscontinued = False
            elif calctype == 3:
                exit()
            else: 
                print("else function 155")
                iscontinued = False
    displayinput(user_prin, user_pmt, user_irate, user_term, user_date)
    
    monthly_irate = user_irate / 12
    months = user_term * 12
    balance = user_prin
    current_date = user_date
    schedule = []

    for month in range(1, months + 1):
        interest = balance * monthly_irate
        principal_paid = user_pmt - interest
        balance -= principal_paid

        schedule.append({
            "Month": month,
            "Date": current_date.strftime("%B %Y"), 
            "Payment": round(user_pmt, 2),
            "Principal Paid": round(principal_paid, 2),
            "Interest Paid": round(interest, 2),
            "Remaining Balance": round(max(balance, 0), 2)
        })
        current_date = add_month(current_date)

    for row in schedule[:12]: #print the first 12 months to review
        print(row)    
    
    schedule_csv = pd.DataFrame(schedule, columns=[
            "Month",
            "Date",
            "Payment",
            "Principal Paid",
            "Interest Paid",
            "Remaining Balance"
        ])

    schedule_csv.to_csv("amortization_schedule.csv", index=False)
    print("CSV exported successfully to amortization_schedule.csv.")

    return schedule

#DISPLAY INPUTS 
def displayinput(user_prin, user_pmt, user_irate, user_term, user_date): #display rounded user inputs
    print("Summary of User Inputs")
    print(f"Principal amount: ${user_prin:.2f}")
    print(f"Payment amount: ${user_pmt:.2f}")
    print(f"Interest rate: {user_irate * 100}%")
    print(f"Term length: {user_term} years")
    print(f"Start Date: {user_date}")
    print("First 12 months of payments:")
    
    return(user_prin, user_pmt, user_irate, user_term, user_date)

#ADD MONTHS
def add_month(d): #adds +1 month to the payment date from the amortization schedule, handles days and years, returns date fields
    year = d.year
    month = d.month + 1

    if month > 12:
        month = 1
        year += 1

    #tried to handle days at end of month (e.g., January 31 → February 28)
    day = min(d.day, [31, 29 if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0) else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31][month-1])

    return date(year, month, day)

#FUNCTION TO GENERATE AMORTIZATION SCHEDULE  
def amortization_schedule(user_prin, user_pmt, user_irate, user_term, user_start):
    monthly_irate = user_irate / 12
    months = user_term * 12
    balance = user_prin
    current_date = user_start
    schedule = []

    for month in range(1, months + 1):
        interest = balance * monthly_irate
        principal_paid = user_pmt - interest
        balance -= principal_paid

        schedule.append({
            "Month #": month,
            "Date": current_date, 
            "Payment": round(user_pmt, 2),
            "Principal Paid": round(principal_paid, 2),
            "Interest Paid": round(interest, 2),
            "Remaining Balance": round(max(balance, 0), 2)
        })
        month += month

    for row in schedule[:12]: #print the first 12 months to review
        print(row)
    
    graph(schedule)

    return schedule

#FUNCTION TO GENERATE A GRAPH
def graph(schedule):
    months = [row["Month"] for row in schedule]
    principal = [row["Principal Paid"] for row in schedule]
    interest = [row["Interest Paid"] for row in schedule]

    splt.figure(figsize=(12, 6))

    splt.stackplot(months, principal, interest, labels=['Principal', 'Interest'])

    splt.title("Mortgage Payment Breakdown Over Time")
    splt.xlabel("Month")
    splt.ylabel("Amount ($)")
    splt.legend(loc='upper right')
    splt.tight_layout()
    splt.show()