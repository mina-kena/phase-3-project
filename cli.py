import click
from models import Session, Category, Product

db = Session()

@click.group()
def cli():
    
    pass

@cli.command()
def init():
    
    print(" Database ready!")

@cli.command()
def add_category():
    
    name = input("Category name: ")
    description = input("Description: ")
    db.add(Category(name=name, description=description))
    db.commit()
    print(f" Added: {name}")

@cli.command()
def list_categories():
    
    print("\n Categories:")
    for cat in db.query(Category).all():
        print(f" - {cat.name}: {cat.description}")