from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()
engine = create_engine("sqlite:///inventory.db")
Session = sessionmaker(bind=engine)

class Category(Base):
    __tablename__ = "categories"
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True)
    description = Column(String(200))

class Product(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    price = Column(Float)
    quantity = Column(Integer)
    category_id = Column(Integer, ForeignKey("categories.id"))


Base.metadata.create_all(engine)