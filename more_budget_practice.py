"""

BEGIN (main() function)
    print Application Header

    # Get User input
    principal = get_principal()
    annual_rate = get_interest_rate()
    years = get_years()

    # Calculate monthly payment using the loan formula
    monthly_payment = calculate_monthly_payment(principal, annual rate, years)
    
    # Display the results in a formatted summary
    display_results(principal, annual_rate, years, monthly_payment)

END

FUNCTION get_principal():
    LOOP until valid input:
        PROMPT "Enter the loan principal amount($): "
        IF input is a valid positive number THEN
            RETURN principal
        ELSE
            PROMPT error message

FUNCTION get_interest_rate():
    LOOP until valid input:
        PROMPT "Enter the annual interest rate (in %, e.g. 5.0 for 5%, or 6.5 for 6.5%): "
        IF input is a valid positive number THEN
            RETURN annual_rate
        ELSE
            PROMPT error message

FUNCTION get_loan_term():
    LOOP until valid input:
        PROMPT "Enter a loan term in years: "
        IF input is a valid positive number THEN
            RETURN years
        ELSE
            PROMPT error message

FUNCTION calculate_monthly_payment(prin, anRate, years):
    monthly_rate = anRate / 12 / 100
    number_of_payments = years * 12
    monthly_payment = (principal * monthly_rate) / (1 - (1 + monthly_rate) ^ (-number_of_payments))
    RETURN monthly_payment

FUNCTION display_results(principal, annual_rate, years, monthly_payment):
    total_payments = years * 12
    total_amount = monthly_payment * total_payments
    PRINT "Loan Payment Summary:"
    PRINT "Loan Principal: $" + formatted principal
    PRINT "Annual Interest: " + formatted annual_rate + "%"
    PRINT "Loan Term: " + years + " years"
    PRINT "Monthly Payment: $" + formatted monthly_payment
    PRINT "Total Payment: $" + formatted total_amount

"""

def main(): # Welcome Statement
    print("\nWelcome to Loan Payment Calculator!\n")



def get_principal():
    while True:
        try:
            principal = float(input("Enter a loan principal amount $"))
            if principal > 0:
                return principal
            else: # Prints this message if the user inputs a negative number. This won't change for the upcoming functions.
                print("\nError! You cannot have a negative value! Please re-enter the amount.\n")

        except ValueError: # Prints this message if the user inputs an invalid value, like a string or symbols.
            print("\nInvalid principal amount! Please re-enter your amount.\n")



def get_interest_rate():
    while True:
        try:
            annual_rate = float(input("\nEnter the annual interest rate (in %, e.g. 6.5 for 6.5%): "))
            if annual_rate > 0:
                return annual_rate
            else:
                print("\nError! You cannot have a negative value! Please re-enter the amount.\n")
        except ValueError:
            print("\nInvalid annual-rate amount! Please re-enter your amount.\n")



def get_loan_term():
    while True:
        try:
            years = int(input("\nEnter a loan term in years: "))
            if years > 0:
                return years
            else:
                print("\nError! You cannot have a negative value! Please re-enter the loan term.\n")
        except ValueError: # Prints this message if the user inputs a string or float or anything but a whole number.
            print("\nInvalid loan-term! Maybe you have entered a decimal? Please re-enter your loan term.\n")


        
def calculate_monthly_payment(principal, annual_rate, years):
    monthly_rate = annual_rate / 12 / 100
    number_of_payments = years * 12
    monthly_payment = (principal * monthly_rate) / (1 - (1 + monthly_rate) ** (-number_of_payments))
    return monthly_payment


def display_summary(principal, annual_rate, years, monthly_payment):
    total_payments = years * 12
    total_amount = monthly_payment * total_payments
    print("-------------------------------")
    print("\n\nYour Loan Payment Summary:\n")
    print(f"Loan Principal: ${principal:.2f}")
    print(f"Annual Interest: {annual_rate:.2f}%")
    print(f"Loan Term: {years} years")
    print(f"Monthly Payment: ${monthly_payment:.2f}")
    print(f"Total Payment: ${total_amount:.2f}")



main()
principal = get_principal()
annual_rate = get_interest_rate()
years = get_loan_term()
monthly_payment = calculate_monthly_payment(principal, annual_rate, years)
display_summary(principal, annual_rate, years, monthly_payment)