import sqlite3
from app.utils.constants import DATABASE_PATH
from app.utils.constants import ALLOWED_COLUMNS
import app.models.expense as expense
class SQLiteRepository:
    def __init__(self,db_name= DATABASE_PATH):
        self.db_name = db_name
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        self.create_table()

    def create_table(self):
        sql = """   CREATE TABLE IF NOT EXISTS expenses (
        e_id TEXT PRIMARY KEY, 
        amount REAL,
        e_date TEXT,
        category TEXT,
        description TEXT,
        payment_method TEXT,
        created_at TEXT)""" 

        self.cursor.execute(sql)
        self.connection.commit()
        print("DB initiation completed")

    def add_expense(self,expense):
        expense_dict = expense.to_dict()
        sql = """INSERT INTO expenses (e_id,amount,e_date,category,description,payment_method,created_at)
        VALUES
            (?,?,?,?,?,?,?)
        
        """
        values = (
        expense_dict["e_id"],
        expense_dict["amount"],
        expense_dict["e_date"],
        expense_dict["category"],
        expense_dict["description"],
        expense_dict["payment_method"],
        expense_dict["created_at"]
    )
        try :
            self.cursor.execute(sql,values)
            self.connection.commit()
        except sqlite3.IntegrityError:
            print(f"SQLite primary key violation , duplicate {expense_dict["e_id"]} value error")   


    def get_all_expenses(self):
        
        sql = """ select * from expenses """

        self.cursor.execute(sql)
        expense_data = self.cursor.fetchall()
        
        expenses_dict=[]
        for row in expense_data:
            expenses_dict.append(self.tuple_to_dict(row))
        expenses = []
        for exp in expenses_dict:
            expenses.append(expense.Expense.from_dict(exp))
        return expenses

            
    def tuple_to_dict(self,data):
        expense_dict= {}
        expense_dict["e_id"] = data[0]
        expense_dict["amount"] = data[1]
        expense_dict["e_date"] = data[2]
        expense_dict["category"] = data[3]
        expense_dict["description"] = data[4]
        expense_dict["payment_method"] = data[5]
        expense_dict["created_at"] = data[6]

        return expense_dict\

    def search_expenses(self,column_name,value):
        if column_name not in ALLOWED_COLUMNS:
            print ("Enter the valis column name to search")
        else:
            sql = f" select * from expenses where {column_name} = ? "
            
            self.cursor.execute(sql,(value,))
            expense_data = self.cursor.fetchall()
            expenses=[]
            for row in expense_data:
                expenses.append(expense.Expense.from_dict(self.tuple_to_dict(row)))
            return expenses
        
    





        

        
         






