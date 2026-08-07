# Software Engineering Dictionary

## Purpose

This document contains software engineering terminology that I learned while building the Expense Management System.

Every concept includes:

- Formal Definition
- Plain English Explanation
- Example from this project

---

# Quick Reference

| Term | Plain English | EMS Example | Status |
|------|---------------|-------------|--------|
| Dependency | Something another class needs to do its job | ExpenseManager needs SQLiteRepository | ✅ |
| Dependency Injection | Give an object instead of creating it | ExpenseManager(repo) | 🟡 Planned |
| Repository | Class responsible for storing and retrieving data | SQLiteRepository | ✅ |
| Business Logic | Rules that control the application | ExpenseManager | ✅ |
| Persistence | Saving data permanently | JSON / SQLite | ✅ |
| Serialization | Object → Dictionary | Expense.to_dict() | ✅ |
| Deserialization | Dictionary → Object | Expense.from_dict() | ✅ |
| Refactoring | Improve code without changing behavior | Reuse one repository object | 🟡 Planned |
| Instantiate | Create an object | SQLiteRepository() | ✅ |
| Source of Truth | Official location of application data | SQLite Database | ✅ |
# Software Engineering Dictionary

| Term | Plain English | Expense Management System (EMS) Example |
|------|---------------|------------------------------------------|
| Trade-off | Choosing between two good solutions, where each has advantages and disadvantages. | Deciding between `search_by_category()`, `search_by_date()`, etc., versus one generic `search_expenses(column_name, value)` method. |
| Parameterized Query | An SQL query where values are passed separately from the SQL statement to improve security and correctness. | `SELECT * FROM expenses WHERE category = ?` followed by `cursor.execute(sql, ("Food",))`. |
| SQL Injection | A security vulnerability where user input changes the meaning of an SQL query. | Writing `f"SELECT * FROM expenses WHERE category = {value}"` instead of using `?` placeholders can allow malicious SQL to execute. |
| Separation of Concerns (SoC) | Each class or module should have one clear responsibility. | `main.py` handles user interaction, `ExpenseManager` handles business logic, and `SQLiteRepository` handles database operations. |
| Exception Propagation | An exception travels up the function call stack until it is handled. | `SQLiteRepository` raises a `ValueError`; if `ExpenseManager` doesn't catch it, it continues to `main.py`, where it can be handled. |
| Source of Truth | The single, authoritative place where data is stored and maintained. | In Version 2, the SQLite database is the source of truth, not `manager.expenses`. |
| Consistency | Similar problems should be solved in a similar way throughout the project. | Storing `DATABASE_PATH`, `JSON_PATH`, and `ALLOWED_COLUMNS` together in `constants.py` keeps configuration organized and predictable. |
| Repository Pattern | A class responsible for all database operations, hiding SQL details from the rest of the application. | `SQLiteRepository` provides methods like `add_expense()`, `get_all_expenses()`, `search_expenses()`, `update_expense()`, and `delete_expense()`. |
| Single Source of Truth | Information should exist in one place to avoid duplication and inconsistency. | `ALLOWED_COLUMNS` is defined only once in `constants.py` instead of being repeated in multiple methods. |
| Refactoring | Improving the internal structure of code without changing its external behavior. | Replacing multiple search methods with a single `search_expenses(column_name, value)` method to reduce duplicate code. |
| Abstraction | Hiding implementation details behind a simpler interface. | `main.py` calls `manager.search_expenses()`, without knowing how SQL queries are executed. |
| API (Application Programming Interface) | The public methods a class exposes for other parts of the program to use. | `ExpenseManager` exposes methods like `add_expense()`, `get_all_expenses()`, and `search_expenses()` for `main.py`. |
| Dependency Injection | Providing an object to a class instead of letting the class create it itself. | `main.py` creates `SQLiteRepository` and passes it to `ExpenseManager` through its constructor instead of `ExpenseManager` creating it internally. |
---

# Detailed Notes

## Dependency

### Definition

A dependency is an object or class that another class needs in order to perform its work.

### Plain English

"If I need another object to do my work, that object is my dependency."

### EMS Example

ExpenseManager depends on SQLiteRepository to access the database.

```text
ExpenseManager
        │
        ▼
SQLiteRepository
```

---

## Dependency Injection

### Definition

Providing a dependency to a class instead of letting the class create it.

### Plain English

"Receive the object instead of creating it."

### EMS Example

Current

```python
repo = SQLiteRepository()
```

Future

```python
repo = SQLiteRepository()
manager = ExpenseManager(repo)
```

ExpenseManager receives the repository instead of creating one.

---

## Repository

...