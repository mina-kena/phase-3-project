# Inventory Management CLI

A simple command-line inventory management system built with Python, SQLAlchemy, and Click. This application allows you to manage product categories and inventory items through an easy-to-use CLI interface.

## Features

- **Category Management**: Add and list product categories
- **Database Integration**: SQLite database with SQLAlchemy ORM
- **CLI Interface**: User-friendly command-line interface using Click
- **Extensible Design**: Easy to add new commands and features

## Project Structure

```
inventory-cli/
├── main.py          # Application entry point
├── cli.py           # CLI commands and interface
├── models.py        # Database models and configuration
├── inventory.db     # SQLite database (created automatically)
└── README.md        # This file
```

## Installation

1. Clone or download the project files

2. Install required dependencies:
   ```bash
   pip install click sqlalchemy
   ```

3. Initialize the database:
   ```bash
   python main.py init
   ```

# Usage

Run the application using Python:

```bash
python main.py [COMMAND]
```

# Available Commands

# Initialize Database
```bash
python main.py init
```
Sets up the database and displays a ready message.

# Add Category
```bash
python main.py add-category
```
Prompts you to enter a category name and description, then adds it to the database.

# List Categories
```bash
python main.py list-categories
```
Displays all categories with their descriptions.

# Example Usage

```bash
#Initialize the database
python main.py init

# Add a new category
python main.py add-category
# Enter: Electronics
# Enter: Electronic devices and accessories

# List all categories
python main.py list-categories
```


# Technical Details

- **Database**: SQLite with SQLAlchemy ORM
- **CLI Framework**: Click for command-line interface
- **Python Version**: Compatible with Python 3.6+



# Development

To extend the application:

1. Add new commands in `cli.py` using the `@cli.command()` decorator
2. Create additional models in `models.py` if needed
3. Use the existing database session (`db`) for database operations

# Requirements

- Python 3.6+
- click
- sqlalchemy

# License

This project is mine.