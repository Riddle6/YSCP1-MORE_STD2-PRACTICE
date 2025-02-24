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
    monthly_payment = (principal * monthly_rate) / (1 - (1 + monthly_rate)) ^ (-number_of_payments)
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

def main():
    print("\nWelcome to Loan Payment Calculator!\n")

def get_principal():
    while True:
        try:
            principal = float(input("Enter a loan principal amount $"))
            if principal > 0:
                return principal
            else:
                print("\nError! You cannot have a negative value! Please re-enter the amount.\n")

        except ValueError:
            print("\nInvalid principal amount! Please re-enter your amount.\n")

def get_interest_rate():
    while True:
        try:
            annual_rate = float(input("\nEnter the annual interest rate: %"))
            if annual_rate > 0:
                return annual_rate
            else:
                print("\nError! You cannot have a negative value! Please re-enter the amount.\n")
        except ValueError:
            print("\nInvalid annual-rate amount! Please re-enter your amount.\n")

def get_loan_term():
    while True:
        try:
            loan_term = int(input("Enter a loan term in years: "))
            if loan_term > 0:
                return loan_term
            else:
                print("\nError! You cannot have a negative value! Please re-enter the loan term.\n")
        except ValueError:
            print("\nInvalid loan-term! Please re-enter your loan term.\n")
        

main()
get_principal()