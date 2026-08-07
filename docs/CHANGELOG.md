# Changelog

All notable changes to the Expense Management System will be documented in this file.

The format is inspired by "Keep a Changelog".

---

# [Version 2.0.0] - In Progress

## Added
- Introduced SQLite as the primary persistence layer.
- Created `SQLiteRepository`.
- Added SQLite database (`expense.db`).
- Implemented database schema creation.
- Reorganized project into a layered architecture.
- Added package structure using `__init__.py`.

## Changed
- Moved project files into logical packages:
  - `models`
  - `services`
  - `repositories`
  - `validators`
  - `utils`
  - `importers`
- Moved `data.json` into the `data/` directory.
- Moved `expense.db` into the `database/` directory.
- Updated imports to use package-based imports.
- Changed application startup to:

```bash
python -m app.main
```

instead of running `main.py` directly.

## Fixed
- Fixed package import errors after project restructuring.
- Updated module imports to match the new folder hierarchy.
- [ ] Rename `file_handler.py` → `json_repository.py`
## Refactor Backlog

The following improvements are intentionally postponed until the core SQLite functionality is complete.

### Repository Layer

- [ ] Standardize repository method names.
- [ ] Introduce a common repository interface.

### File Paths
- [ ] Replace hardcoded paths with `pathlib.Path`.
- [ ] Centralize application paths.

### Import System
- [ ] Implement `JSONImporter`.
- [ ] Support importing JSON into SQLite.
- [ ] Design importer architecture for future CSV and Excel support.

### Application Structure
- [ ] Reduce responsibilities inside `main.py`.
- [ ] Move business logic completely into the service layer.
- [ ] Review package exports (`__init__.py`).

### Error Handling
- [ ] Replace generic `except` blocks with specific exceptions.
- [ ] Improve validation messages.
- [ ] Add logging.

### Testing
- [ ] Create unit tests.
- [ ] Create repository tests.
- [ ] Create importer tests.

---

# [Version 1.0.0]

## Added
- Expense Management System (Console)
- CRUD operations
- JSON persistence
- UUID-based Expense model
- Statistics module
- Matplotlib charts
- Input validation
- Modular OOP architecture
