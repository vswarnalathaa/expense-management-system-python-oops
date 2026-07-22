import json
import expense

def load_data():
    try:
        with open(r'data.json', 'r') as file:
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

    with open(r'data.json', 'w') as file:
        json.dump(exp_dicts,file, indent=4) 