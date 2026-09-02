

class ExpenseManager:
 
    def __init__(self,repo):
        self.repo = repo
        
        
    def add_expense(self,expense):
        
        self.repo.add_expense(expense)
        

    
    def search_expenses(self,column_name,value):
        
        exp_list = self.repo.search_expenses(column_name,value)
        return exp_list  
           
                
    def delete_expense(self,expense):
        
        self.repo.delete_expense(str(expense.e_id))
    
    def get_all_expenses(self):
        
        return self.repo.get_all_expenses()
        
    
    def update_expense(self,expense,column_name,value):
         self.repo.update_expense(str(expense.e_id),column_name,value)
         
         


   

            
    
