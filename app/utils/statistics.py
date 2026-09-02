
class Statistics:
    
    def __init__(self,repo):
        self.repo = repo
    
    def no_of_records(self):
        
        return (self.repo.total_records())
    
    def total_amount(self):
        
        return (self.repo.total_amount())
    
    def highest_expense(self):
        
        return (self.repo.highest_expense())
    
    def lowest_expense(self):
       
        return (self.repo.lowest_expense())
    
    def average_expense(self):
        
        return (self.repo.average_expense())
    
    def category_summary(self):
        
        return (self.repo.category_summary())
    
    def payment_method_summary(self):
        
        return (self.repo.payment_method_summary())
    
    def month_by_summary(self):
       
        return (self.repo.month_by_summary())
