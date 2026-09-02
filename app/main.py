
import app.validators.validation as validation

import app.services.expense_manager as expense_manager
import app.models.expense as expense
from app.utils.constants import STAT_OPTIONS
import app.utils.statistics as statistics
import app.utils.display as display
import app.utils.chart as chart
import app.repositories.sqlite_repository as sqlite_repository

# import statistic

def handle_delete_expense(manager):
    while True:
                    opt = validation.get_valid_option(f"1. Delete by Category\n2. Delete by Date\n3. Cancel\nChoose a option : ")
                    if opt == 1:
                        cat = validation.get_valid_category("enter the category to be Deleted : ")
                        exp_list = manager.search_expenses('category',cat)
                        if not exp_list :
                            print("No Expense found ")
                            
                        else :
                            for index, exp in enumerate(exp_list):
                                print(f"{index + 1}. | {exp.compact_display()}")
                            opt_del = validation.get_valid_record("Select a Record to delete : ", len(exp_list))
                            manager.delete_expense(exp_list[opt_del-1])
                            
                    elif opt == 2 :
                        search_date = validation.get_valid_date("Enter the Date to be Deleted : ")
                        exp_list =  manager.search_expenses('e_date',search_date)
                        if not exp_list :
                            print("No Expense found ")
                        else :
                            for index, exp in enumerate(exp_list):
                                print(f"{index + 1}. | {exp.compact_display()}")
                                #exp.compact_display()
                            opt_del = validation.get_valid_record("Select a Record to delete : ",len(exp_list))
                            manager.delete_expense(exp_list[opt_del-1])
                            
                    else:
                        break

def handle_search_expense(manager):
    while True:
                    opt = validation.get_valid_option(f"1. search by Category\n2. Search by Date\n3. cancel\nChoose a option")
                    if opt == 1:
                        cat = validation.get_valid_category("enter the category to be searched : ")
                        exp_list = manager.search_expenses('category',cat)
                        if not exp_list :
                            print("No Expense found ")
                        else :
                            for exp in exp_list:
                                exp.display()
                    elif opt == 2 :
                        search_date = validation.get_valid_date("Enter the Date to be searched : ")
                        exp_list = manager.search_expenses('e_date',search_date)
                        if not exp_list :
                            print("No Expense found ")
                        else :
                            for exp in exp_list:
                                exp.display()
                    else:
                        break

def handle_update_expense(manager):
     while True:
                    opt = validation.get_valid_option(f"1. Update by Category\n2. Update by Date\n3. Cancel\nChoose a option: ")
                    if opt == 1:
                        cat = validation.get_valid_category("enter the category : ")
                        exp_list = manager.search_expenses('category',cat)
                        if not exp_list :
                            print("No Expense found ")
                            
                        else :
                            for index, exp in enumerate(exp_list):
                                print(f"{index + 1}. | {exp.compact_display()}")
                            opt = validation.get_valid_record("Select a Record to Update : ", len(exp_list))
                            while True:
                                value = validation.get_valid_update_option(f"1. Amount\n2. Date\n3. Category\n4. Description\n5. Payment Method\n6. Cancel\nSelect the field to be updated: ")
                                if value == 1:
                                    amount = validation.get_valid_amount("Enter the valid Amount : ")
                                    manager.update_expense(exp_list[opt-1],"amount",amount)
                                    print("Expense is updated successfully")
                                elif value == 2:    
                                    date = validation.get_valid_date("Enter the valid date yyyy-mm-dd : ")
                                    manager.update_expense(exp_list[opt-1],"e_date",date)
                                    print("Expense is updated successfully")
                                elif value == 3:
                                    category = validation.get_valid_category("Enter the valid category : ")
                                    manager.update_expense(exp_list[opt-1],"category",category)
                                    print("Expense is updated successfully")
                                elif value == 4:
                                    description = validation.get_valid_string("Enter the valid description : ")
                                    manager.update_expense(exp_list[opt-1],"description",description)
                                    print("Expense is updated successfully")
                                elif value == 5:
                                    payment = validation.get_valid_payment("Enter the valid payment type : ")  
                                    manager.update_expense(exp_list[opt-1],"payment_method",payment)
                                    print("Expense is updated successfully")
                                else:
                                    break  
                                
                    elif opt == 2 :
                        search_date = validation.get_valid_date("Enter the Date : ")
                        exp_list = manager.search_expenses('e_date',search_date)
                        if not exp_list :
                            print("No Expense found ")
                        else :
                            for index, exp in enumerate(exp_list):
                                print(f"{index + 1}. | {exp.compact_display()}")
                                #exp.compact_display()
                            opt_del = validation.get_valid_record("Select a Record to Update : ", len(exp_list))
                            while True:
                                value = validation.get_valid_update_option(f"1. Amount\n2. Date\n3. Category\n4. Description\n5. Payment Method\n6. Cancel\nSelect the field to be updated: ")
                                if value == 1:
                                    amount = validation.get_valid_amount("Enter the valid Amount : ")
                                    manager.update_expense(exp_list[opt_del-1],"amount",amount)
                                    print("Expense is updated successfully")    
                                elif value == 2:    
                                    date = validation.get_valid_date("Enter the valid date yyyy-mm-dd : ")
                                    manager.update_expense(exp_list[opt_del-1],"e_date",date)
                                    print("Expense is updated successfully")   
                                elif value == 3:
                                    category = validation.get_valid_category("Enter the valid category : ")
                                    manager.update_expense(exp_list[opt_del-1],"category",category)
                                    print("Expense is updated successfully")
                                elif value == 4:
                                    description = validation.get_valid_string("Enter the valid description : ")
                                    manager.update_expense(exp_list[opt_del-1],"description",description)
                                    print("Expense is updated successfully")    
                                elif value == 5:
                                    payment = validation.get_valid_payment("Enter the valid payment type : ")  
                                    manager.update_expense(exp_list[opt_del-1],"payment_method",payment)
                                    print("Expense is updated successfully")    
                                else:
                                    break  
                            
                    else:
                        break

def handle_statistics_expense(repo):
    stat = statistics.Statistics(repo)
    while True:
        sat_opt = validation.get_valid_stat_option(f"--------------Statistics----------\n1. Summary Statistics\n2. Category Wise Summary\n3. Payment Method Wise summary\n4. Monthly Spending\n5. Chart\n6. Exit\nChoose an Option : ")
        if sat_opt == 1:
            no_of_records = stat.no_of_records()
            print(f"Total No.Of Records : {no_of_records}")
            total_amount = stat.total_amount()
            print(f"Total Amount : {total_amount}")
            print(f"Highest Expense\n-----------------\n")
            for exp in stat.highest_expense():
                
                print(exp.compact_display())
            #print(f"Highest Expense :\n {stat.highest_expense().compact_display()}")
            #print(f"Lowest Expense :\n {stat.lowest_expense().compact_display()}")
            print(f"Lowest Expense\n-----------------\n")
            for exp in stat.lowest_expense():
                                    
                print(exp.compact_display())
            average_expense = stat.average_expense()
            print(f"Average Expense : {average_expense}")

        elif sat_opt == 2:
            data = stat.category_summary()
            display.display_dict("Category Wise Summary",data)

        elif sat_opt == 3:
            data = stat.payment_method_summary()
            display.display_dict("Payment Method Wise Summary",data)
        elif sat_opt == 4:
            data = stat.month_by_summary()
            display.display_dict("Month wise Summary",data)
        elif sat_opt == 5:
            while True:
                chart_opt = validation.get_valid_chart_option(f"------------- Charts-----------\n1. Category Summary Chart\n2. Payment Mathod Summary Chart\n3. Monthly Summary Chart\n4. Exit\n Choose an Option : ")
                if chart_opt == 1:
                    data = stat.category_summary()
                    chart.category_summary_chart(data)
                elif chart_opt == 2:
                    data = stat.payment_method_summary()
                    chart.payment_method_summary_chart(data)
                elif chart_opt == 3:
                    data = stat.month_by_summary()
                    chart.monthly_summary_chart(data)
                else:
                    break

                

        else :
                break

def handle_add_expense(manager):
    amount = validation.get_valid_amount("Enter the valid Amount")
    date = validation.get_valid_date("Enter the valid date yyyy-mm-dd")
    category = validation.get_valid_category("Enter the valid category")
    description = validation.get_valid_string("Enter the valid description")
    payment = validation.get_valid_payment("Enter the valid payment type")
    
    exp = expense.Expense(amount, date, category, description, payment)
    
    manager.add_expense(exp) 

def handle_get_all_expense(manager):
    expenses = manager.get_all_expenses()
    for exp in expenses:
        exp.display()


def main():
   
    repo = sqlite_repository.SQLiteRepository()
    manager = expense_manager.ExpenseManager(repo)
    try:
        while True:
            
            menu = validation.get_valid_menu_option(f"-----------------Expense Management System-------------------\n1. Add Expense\n2. View all Expense\n3. Search Expense\n4. Update expense detail\n5. Delete expense \n6. Staistics\n7. Exit\nEnter the option: ")
            if menu == 1:
                handle_add_expense(manager)
            
            elif menu == 2:
                handle_get_all_expense(manager)
                
            elif menu == 3:
                handle_search_expense(manager)
                        
            elif menu == 4:
            
                handle_update_expense(manager)

            elif menu == 5:
                handle_delete_expense(manager)
            

            elif menu == 6:
                handle_statistics_expense(repo)
                
            else:
                break
    finally:
         repo.close()
   

if __name__ == "__main__":
    main()