import json
import os
# import calculations
import validation
import file_handler
import expense_manager
import expense
from constants import STAT_OPTIONS
import statistics
import display
import chart

# import statistic

def main():
    manager = expense_manager.ExpenseManager()
    manager.expenses = file_handler.load_data() 
    #print(type(manager.expenses))
    # print(type(manager.expenses))
    # print(manager.expenses) 
    while True:
        
        menu = validation.get_valid_menu_option(f"-----------------Expense Management System-------------------\n1. Add Expense\n2. View all Expense\n3. Search Expense\n4. Update expense detail\n5. Delete expense \n6. Staistics\n7. Exit\nEnter the option: ")
        if menu == 1:
            amount = validation.get_valid_amount("Enter the valid Amount")
            date = validation.get_valid_date("Enter the valid date yyyy-mm-dd")
            category = validation.get_valid_category("Enter the valid category")
            description = validation.get_valid_string("Enter the valid description")
            payment = validation.get_valid_payment("Enter the valid payment type")
         
            exp = expense.Expense(amount, date, category, description, payment)
            
            manager.add_expense(exp)
            file_handler.save_data(manager.expenses)
                      
        elif menu == 2:
            manager.get_all_expenses()
        elif menu == 3:
            if not manager.expenses:
                print ("No expenses found")
            else:
                while True:
                    opt = validation.get_valid_option(f"1.search by Category\n2.Search by Date\n3. cancel\n Choose a option")
                    if opt == 1:
                        cat = validation.get_valid_category("enter the category to be searched : ")
                        exp_list = manager.search_expense_bycategory(cat)
                        if not exp_list :
                            print("No Expense found ")
                        else :
                            for exp in exp_list:
                                exp.display()
                    elif opt == 2 :
                        search_date = validation.get_valid_date("Enter the Date to be searched : ")
                        exp_list = manager.search_expense_bydate(search_date)
                        if not exp_list :
                            print("No Expense found ")
                        else :
                            for exp in exp_list:
                                exp.display()
                    else:
                        break
                    # if s == None:
            #     print("student does not exist")  
            # else:
            #     student_func.display_report(s)
        elif menu == 4:
            if not manager.expenses:
                print ("No expenses found")
            else:
                while True:
                    opt = validation.get_valid_option(f"1.Update by Category\n2.Update by Date\n3. Cancel\nChoose a option: ")
                    if opt == 1:
                        cat = validation.get_valid_category("enter the category : ")
                        exp_list = manager.search_expense_bycategory(cat)
                        if not exp_list :
                            print("No Expense found ")
                            
                        else :
                            for index, exp in enumerate(exp_list):
                                print(f"{index + 1}. | {exp.compact_display()}")
                            opt_del = validation.get_valid_optdel("Select a Record to Update", len(exp_list))
                            while True:
                                value = validation.get_valid_update_option(f"1. Amount\n2. Date\n3. Category\n4. Description\n5. Payment Method\n6. Cancel\n Select the field to be updated: ")
                                if value == 1:
                                    amount = validation.get_valid_amount("Enter the valid Amount")
                                    manager.update_expense(exp_list[opt_del-1],"amount",amount)
                                    file_handler.save_data(manager.expenses)
                                    print("Expense is updated successfully")
                                elif value == 2:    
                                    date = validation.get_valid_date("Enter the valid date yyyy-mm-dd")
                                    manager.update_expense(exp_list[opt_del-1],"e_date",date)
                                    file_handler.save_data(manager.expenses)
                                    print("Expense is updated successfully")
                                elif value == 3:
                                    category = validation.get_valid_category("Enter the valid category")
                                    manager.update_expense(exp_list[opt_del-1],"category",category)
                                    file_handler.save_data(manager.expenses)
                                    print("Expense is updated successfully")
                                elif value == 4:
                                    description = validation.get_valid_string("Enter the valid description")
                                    manager.update_expense(exp_list[opt_del-1],"description",description)
                                    file_handler.save_data(manager.expenses)
                                    print("Expense is updated successfully")
                                elif value == 5:
                                    payment = validation.get_valid_payment("Enter the valid payment type")  
                                    manager.update_expense(exp_list[opt_del-1],"payment_method",payment)
                                    file_handler.save_data(manager.expenses)
                                    print("Expense is updated successfully")
                                else:
                                    break  
                                
                    elif opt == 2 :
                        search_date = validation.get_valid_date("Enter the Date : ")
                        exp_list = manager.search_expense_bydate(search_date)
                        if not exp_list :
                            print("No Expense found ")
                        else :
                            for index, exp in enumerate(exp_list):
                                print(f"{index + 1}. | {exp.compact_display()}")
                                #exp.compact_display()
                            opt_del = validation.get_valid_optdel("Select a Record to Update", len(exp_list))
                            while True:
                                value = validation.get_valid_update_option(f"1. Amount\n2. Date\n3. Category\n4. Description\n5. Payment Method\n6. Cancel\n Select the field to be updated: ")
                                if value == 1:
                                    amount = validation.get_valid_amount("Enter the valid Amount")
                                    manager.update_expense(exp_list[opt_del-1],"amount",amount)
                                    file_handler.save_data(manager.expenses)
                                    print("Expense is updated successfully")    
                                elif value == 2:    
                                    date = validation.get_valid_date("Enter the valid date yyyy-mm-dd")
                                    manager.update_expense(exp_list[opt_del-1],"e_date",date)
                                    file_handler.save_data(manager.expenses)
                                    print("Expense is updated successfully")   
                                elif value == 3:
                                    category = validation.get_valid_category("Enter the valid category")
                                    manager.update_expense(exp_list[opt_del-1],"category",category)
                                    file_handler.save_data(manager.expenses)
                                    print("Expense is updated successfully")
                                elif value == 4:
                                    description = validation.get_valid_string("Enter the valid description")
                                    manager.update_expense(exp_list[opt_del-1],"description",description)
                                    file_handler.save_data(manager.expenses)
                                    print("Expense is updated successfully")    
                                elif value == 5:
                                    payment = validation.get_valid_payment("Enter the valid payment type")  
                                    manager.update_expense(exp_list[opt_del-1],"payment_method",payment)
                                    file_handler.save_data(manager.expenses)
                                    print("Expense is updated successfully")    
                                else:
                                    break  
                           
                    else:
                        break
        elif menu == 5:
            if not manager.expenses:
                print ("No expenses found")
            else:
                while True:
                    opt = validation.get_valid_option(f"1.Delete by Category\n2.Delete by Date\n3. Cancel\nChoose a option")
                    if opt == 1:
                        cat = validation.get_valid_category("enter the category to be Deleted : ")
                        exp_list = manager.search_expense_bycategory(cat)
                        if not exp_list :
                            print("No Expense found ")
                            
                        else :
                            for index, exp in enumerate(exp_list):
                                print(f"{index + 1}. | {exp.compact_display()}")
                            opt_del = validation.get_valid_optdel("Select a Record to delete", len(exp_list))
                            manager.delete_expense(exp_list[opt_del-1])
                            file_handler.save_data(manager.expenses)
                    elif opt == 2 :
                        search_date = validation.get_valid_date("Enter the Date to be Deleted : ")
                        exp_list = manager.search_expense_bydate(search_date)
                        if not exp_list :
                            print("No Expense found ")
                        else :
                            for index, exp in enumerate(exp_list):
                                print(f"{index + 1}. | {exp.compact_display()}")
                                #exp.compact_display()
                            opt_del = validation.get_valid_optdel("Select a Record to delete")
                            manager.delete_expense(exp_list[opt_del-1])
                            file_handler.save_data(manager.expenses)
                    else:
                        break
        elif menu == 6:
            if not manager.expenses:
                print("No expenses available.")
            else:
                stat = statistics.Statistics()
                while True:
                    sat_opt = validation.get_valid_stat_option(f"--------------Statistics----------\n1. Summary Statistics\n2. Category Wise Summary\n3. Payment Method Wise summary\n4. Monthly Spending\n5. Chart\n6. Exit\nChoose an Option : ")
                    if sat_opt == 1:
                        no_of_records = stat.no_of_records(manager.expenses)
                        print(f"Total No.Of Records : {no_of_records}")
                        total_amount = stat.total_amount(manager.expenses)
                        print(f"Total Amount : {total_amount}")
                        print(f"Highest Expense :\n {stat.highest_expense(manager.expenses).compact_display()}")
                        print(f"Lowest Expense :\n {stat.lowest_expense(manager.expenses).compact_display()}")
                        average_expense = stat.average_expense(manager.expenses)
                        print(f"Average Expense : {average_expense}")

                    elif sat_opt == 2:
                        data = stat.category_summary(manager.expenses)
                        display.display_dict("Category Wise Summary",data)

                    elif sat_opt == 3:
                        data = stat.payment_method_summary(manager.expenses)
                        display.display_dict("Payment Method Wise Summary",data)
                    elif sat_opt == 4:
                        data = stat.month_by_summary(manager.expenses)
                        display.display_dict("Month wise Summary",data)
                    elif sat_opt == 5:
                        while True:
                            chart_opt = validation.get_valid_chart_option(f"------------- Charts-----------\n1. Category Summary Chart\n2. Payment Mathod Summary Chart\n3. Monthly Summary Chart\n4. Exit\n Choose an Option : ")
                            if chart_opt == 1:
                                data = stat.category_summary(manager.expenses)
                                chart.category_summary_chart(data)
                            elif chart_opt == 2:
                                data = stat.payment_method_summary(manager.expenses)
                                chart.payment_method_summary_chart(data)
                            elif chart_opt == 3:
                                data = stat.month_by_summary(manager.expenses)
                                chart.monthly_summary_chart(data)
                            else:
                                break

                        

                    else :
                        break
        else:
           break
   

    #print(os.getcwd())
    #print(total)
    #print(percentage)
    #print(grade)
    #print(student)



if __name__ == "__main__":
    main()