
class Statistics:
    
    def __init__(self):
        pass
    
    def no_of_records(self,expenses):
        return len(expenses)
    
    def total_amount(self,expenses):
        total = 0
        for exp in expenses:
            total = total+exp.amount
        return total
    
    def highest_expense(self,expenses):
        high_exp= expenses[0]
        for exp in expenses:
            if exp.amount > high_exp.amount:
                high_exp = exp
        return high_exp
    
    def lowest_expense(self,expenses):
        low_exp= expenses[0]
        for exp in expenses:
            if exp.amount < low_exp.amount:
                low_exp = exp
        return low_exp
    
    def average_expense(self,expenses):
        average_exp = self.total_amount(expenses)/self.no_of_records(expenses)
        return average_exp
    
    def category_summary(self,expenses):
        cat_summ ={}
        
        for exp in expenses:
            category = exp.category
            if category in cat_summ:
                cat_summ[category] = cat_summ[category]+exp.amount
            else:
                cat_summ[category]=exp.amount
        return cat_summ
    
    def payment_method_summary(self,expenses):
        pm_summary ={}
        
        for exp in expenses:
            payment_method = exp.payment_method
            if payment_method in pm_summary:
                pm_summary[payment_method] = pm_summary[payment_method]+exp.amount
            else:
                pm_summary[payment_method]=exp.amount
        return pm_summary
    
    def month_by_summary(self,expenses):
        month_summ = {}
        for exp in expenses:
            month = exp.e_date[:7]
            if month in month_summ:
                month_summ[month] = month_summ[month]+exp.amount
            else:
                month_summ[month] = exp.amount
        return month_summ
