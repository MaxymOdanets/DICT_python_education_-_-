import math


class BrainOfCalc:
    @staticmethod
    def calc_diff_payments(periods: int, principal: float, interest: float) -> None:
        overpayment = 0
        monthly_interest_rate = interest / 12
        monthly_principal = principal / periods

        for period in range(periods):
            unpaid_principal = principal - monthly_principal * period
            interest_current = monthly_interest_rate * unpaid_principal
            monthly_payment = math.ceil(monthly_principal + interest_current)
            overpayment += monthly_payment
            print(f"Month {period + 1}: payment is {monthly_payment}")

        print(f"Overpayment: {math.ceil(overpayment - principal)}")
    @staticmethod
    def n_type():
        loan_principal = float(input("Enter the loan principal\n >"))
        monthly_payment = float(input("Enter the monthly payment\n >"))
        loan_interest = float(input("Enter the loan interest\n >")) / 1200
        n = math.ceil(math.log(monthly_payment / (monthly_payment - loan_interest *
                                                  loan_principal), 1 + loan_interest))
        years, month = divmod(n, 12)
        if years == 0:
            print(f"It will take {month} month to repay this loan!")
        elif month == 0:
            print(f"It will take {years} years to repay this loan!")
        else:
            print(f"It will take {years} years and {month} months to repay this loan!")

    @staticmethod
    def a_type():
        loan_principal = float(input("Enter the loan principal\n >"))
        num = float(input("Enter the number of periods\n >"))
        loan_interest = float(input("Enter the loan interest\n >")) / 1200
        annuity_payment = loan_principal * (loan_interest * (1 + loan_interest) ** num) / \
            ((1 + loan_interest) ** num - 1)
        years, months = divmod(num, 12)
        if years == 0:
            print(f"You need to pay {annuity_payment} per month for {months} months")
        elif months == 0:
            print(f"You need to pay {round(annuity_payment)} per month for {years} years")
        else:
            print(f"You need to pay {round(annuity_payment)} per month for {years} years and {months} months")

    @staticmethod
    def p_type():
        annuity_payment = float(input("Enter the annuity_payment\n >"))
        num = float(input("Enter the number of periods\n >"))
        loan_interest = float(input("Enter the loan interest\n >")) / 1200
        loan_principal = annuity_payment / ((loan_interest * (1 + loan_interest) ** num) /
                                            ((1 + loan_interest) ** num - 1))
        years, months = divmod(num, 12)
        if years == 0:
            print(f"Your loan principal = {round(loan_principal)} with {months} months to repay")
        elif months == 0:
            print(f"Your loan principal = {round(loan_principal)} with {years} years to repay")
        else:
            print(f"Your loan principal = {round(loan_principal)} with {years} years and {months} months to repay")
