
import app.repositories.sqlite_repository as sqlite_repository
import app.repositories.json_repository as json_repository
import app.services.expense_manager as expense_manager

def import_json_to_database():
    manager = expense_manager.ExpenseManager()
    
    manager.expenses = json_repository.load_data() 
    repo = sqlite_repository.SQLiteRepository()

    for expense in manager.expenses:
        repo.add_expense(expense)



if __name__ == "__main__":
    import_json_to_database()









