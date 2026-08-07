import json
import app.models.expense as expense
from app.utils.constants import JSON_PATH

def load_data():
    try:
        with open(JSON_PATH, 'r') as file:
            expenses=[]
            data = json.load(file)
            for d in data:
                expenses.append(expense.Expense.from_dict(d))
            return expenses
    
    except Exception as e:
        print(type(e))
        print(e)
        
def save_data(expenses):
    exp_dicts=[]
    for exp in expenses:
        exp_dicts.append(exp.to_dict())

    with open(JSON_PATH, 'w') as file:
        json.dump(exp_dicts,file, indent=4) 