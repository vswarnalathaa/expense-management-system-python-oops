from datetime import date
from app.utils.constants import CATEGORIES
from app.utils.constants import PAYMENT_METHODS
from app.utils.constants import MENU_OPTIONS
from app.utils.constants import STAT_OPTIONS


def get_valid_amount(prompt):
    while True:
        try:
            amount = float(input(prompt))
            if amount > 0 :
                return amount
            else:
                print ("Enter the amount greater the 0")
        except ValueError:
            print ("Enter the amount greater the 0")

def get_valid_date(prompt):
    while True:
        try:
            date_string = input(prompt)
            date.fromisoformat(date_string)
            return date_string
        except ValueError:
            print("enter the valid date in format yyyy-mm-dd")


def get_valid_string(prompt):
    while True:
        valid_string = input(prompt).strip().title()
        if len(valid_string) > 0:
                return valid_string
        else:
            print ("Input cannot be empty")



def get_valid_category(prompt):
    while True:
        value = input(prompt).strip().title()
        if value in CATEGORIES:
            return value
        else:
            print(f"Invalid category. Choose from: {CATEGORIES}")       


def get_valid_payment(prompt):
    while True:
        value = input(prompt).strip().title()
        if value in PAYMENT_METHODS:
            return value
        else:
            print(f"Invalid payment method. Choose from: {PAYMENT_METHODS}")


def get_valid_menu_option(prompt):
    while True:
        try:
            menu = int(input(prompt))
            if menu in MENU_OPTIONS: 
                return menu
            else:
                print("Please choose an option between 1 and 7.")               
        except ValueError:
            print(f"Invalid Menu option . Choose from {MENU_OPTIONS} ")

def get_valid_option(prompt):
    while True:
        try:
            menu = int(input(prompt))
            if 0 < menu <=3 : 
                return menu
            else:
               print(f"Please choose option 1 or 3.")               
        except ValueError:
            print(f"Please choose option 1 or 3.")

def get_valid_optdel(prompt,length):    
    while True:
        try:
            menu = int(input(prompt))
            if 0 < menu <= length : 
                return menu
            else:
               print(f"Please choose option between 1 and {length}")               
        except ValueError:
            print(f"Please choose option between 1 and {length} ")

def get_valid_update_option(prompt):
    while True:
        try:

            update_option = int(input(prompt))
            if 0 < update_option <=6:
                return update_option
            else :
                print(f"Please choose option between 1 and 6")
        except ValueError:
            print(f"Please choose option between 1 and 6")    


def get_valid_stat_option(prompt):
    while True:
        try:
            opt = int(input(prompt))
            if opt in STAT_OPTIONS: 
                return opt
            else:
                print("Please choose an option between 1 and 5.")
                           
        except ValueError:
            print(f"Invalid Menu option . Choose from {STAT_OPTIONS} ")


def get_valid_chart_option(prompt):
    while True:
        try:
            chart_option = int(input(prompt))
            if 0 < chart_option <=4:
                return chart_option
            else :
                print(f"Please choose option between 1 and 4")
        except ValueError:
            print(f"Please choose option between 1 and 4")  