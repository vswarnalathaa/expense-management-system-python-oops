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

        return expense_dict

    def search_expenses(self,column_name,value):
        if column_name not in ALLOWED_COLUMNS:
            print ("Enter the valid column name to search")
            return []
        else:
            sql = f" select * from expenses where {column_name} = ? "
            
            self.cursor.execute(sql,(value,))
            expense_data = self.cursor.fetchall()
            expenses=[]
            for row in expense_data:
                expenses.append(expense.Expense.from_dict(self.tuple_to_dict(row)))
            return expenses
        
    def update_expense(self,e_id,column_name,value):
        if column_name not in ALLOWED_COLUMNS:
            print ("Enter the valid column name to search")
            return []
        else:
            sql = f" update expenses set {column_name} = ? where e_id = ? "
            
            self.cursor.execute(sql,(value,e_id))
            self.connection.commit()
            
    def delete_expense(self,e_id):
        sql = f" delete from expenses where e_id = ? "
            
        self.cursor.execute(sql,(e_id,))
        self.connection.commit()    
    def rows_to_summary_dict(self, rows):
        summary = {}
        for row in rows:
            summary[row[0]] = row[1]
        return summary

    def total_records(self):
        sql = "SELECT COUNT(*) FROM expenses"
        self.cursor.execute(sql)
        row = self.cursor.fetchone()
        return row[0]
    def total_amount(self):
        sql = " SELECT SUM(amount) from expenses"
        self.cursor.execute(sql)
        row = self.cursor.fetchone()
        return row[0]
    
    def highest_expense(self):
        sql = """SELECT *
            FROM expenses
            WHERE amount = (SELECT MAX(amount) FROM expenses)"""
        
        self.cursor.execute(sql)
        rows = self.cursor.fetchall()
        expenses = []

        for row in rows:
            expense_dict = self.tuple_to_dict(row)
            expenses.append(expense.Expense.from_dict(expense_dict))

        return expenses
    
    def lowest_expense(self):
        sql = """SELECT *
            FROM expenses
            WHERE amount = (SELECT MIN(amount) FROM expenses)"""
        
        self.cursor.execute(sql)
        rows = self.cursor.fetchall()
        expenses = []

        for row in rows:
            expense_dict = self.tuple_to_dict(row)
            expenses.append(expense.Expense.from_dict(expense_dict))

        return expenses
               
    def average_expense(self):
        sql = "SELECT AVG(amount) from expenses"
        self.cursor.execute(sql)
        row=self.cursor.fetchone()
        return(row[0])
    def category_summary(self):
        sql = "SELECT category,SUM(amount) from expenses GROUP BY category"
        self.cursor.execute(sql)
        rows = self.cursor.fetchall()
        return(self.rows_to_summary_dict(rows))
    def payment_method_summary(self):
        sql = "SELECT payment_method,SUM(amount) from expenses GROUP BY payment_method"
        self.cursor.execute(sql)
        rows = self.cursor.fetchall()
        return(self.rows_to_summary_dict(rows))
    def month_by_summary(self):
        sql = "SELECT strftime('%Y-%m', e_date),SUM(amount) from expenses GROUP BY strftime('%Y-%m', e_date)"
        self.cursor.execute(sql)
        rows = self.cursor.fetchall()
        return(self.rows_to_summary_dict(rows))

    def close(self):
        self.connection.close()
        

        
         






