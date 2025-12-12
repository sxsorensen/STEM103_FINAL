# STEM103 Final_Project
Final project for a STEM 103 in Fall 2025 taught by Christine Sutton. 

# ABOUT THE AUTHOR
My name is Stacy Sorensen and I'm a student learning Python at Everett Community College.

# ABOUT THE PROGRAM
Program created to calculate a payment or principal amount for a loan. Uses simple interest in the calculation and outputs the payment schedule to a CSV file. One new thing I learned in doing this project was using functions from the datetime library including date, today, and strptime. Also utilized Pandas to more easily convert the data to columns for export. I faced challenges in validating the user inputs and utilized try/except to limit the invalid data passed to the calculator. I tested each function individually and displayed inputs at each step, then compared my math outputs to what Excel generates using PMT and PV functions. Another challenge was in creating the schedule and trying to adjust the dates logically, so I created a function to help process the month rollforward.

If I spent more time on this program, I would like to add a daily interest calculation that accurately accounts for the days between payments and calculates interest accordingly. I'd also like to add the ability to add additional fees, or early payment options.  

Sources:
https://docs.python.org/3/library/datetime.html
https://www.w3schools.com/python/python_datetime.asp
https://www.w3schools.com/python/python_math.asp
https://www.geeksforgeeks.org/python/python-datetime-module/

