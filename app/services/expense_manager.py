import app.models.expense as expense
import app.repositories.sqlite_repository  as sqlite_repository

class ExpenseManager:
 
    def __init__(self,repo):
        self.repo = repo
        self.expenses=[]
        
    def add_expense(self,expense):
        self.expenses.append(expense) 
        

    
    def search_expenses(self,column_name,value):
        
        exp_list = self.repo.search_expenses(column_name,value)
        return exp_list  
           
    def search_expense_bydate(self,e_date):
        exp_list=[]
        for exp in self.expenses:
            if exp.e_date == e_date:
                  exp_list.append(exp)
    
        return exp_list    
        
            
    def delete_expense(self,expense):
        
            self.expenses.remove(expense)
            print("expense removed succefully")
    
    def get_all_expenses(self):
        
        self.expenses = self.repo.get_all_expenses()
        print(f"total no.of expenses = {len(self.expenses)}")
        for exp in self.expenses:
            exp.display()
    
    def update_expense(self,expense,key,value):
         setattr(expense, key, value)
         
         


    #     amount = input("Enter the amount :")
    #     expense_date = input("Enter the expense date")
    #     category = input("Enter the category")
    #     description = input("Enter the expense description")
    #     payment_method = input ("Enter the payment method")

            
    
