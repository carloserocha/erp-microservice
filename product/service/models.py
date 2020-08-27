from sqlalchemy import (DECIMAL, Column, DateTime, ForeignKey, Integer, String)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
import datetime

class Base(object):
    created_at = Column(
        DateTime,
        default=datetime.datetime.utcnow,
        nullable=False
    )
    updated_at = Column(
        DateTime,
        default=datetime.datetime.utcnow,
        onupdate=datetime.datetime.utcnow,
        nullable=False
    )

DeclarativeBase = declarative_base(cls=Base)

class Product(DeclarativeBase):
    __tablename__ = 'product'

    sku = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100))
    description = Column(String(500))
    short_description = Column(String(150))
    reference = Column(String(20))
    warehouse_id = Column(
        Integer,
        ForeignKey('warehouse.id', name='warehouse_id'),
        nullable=False
    )
    
class Warehouse(DeclarativeBase):
    __tablename__ = 'warehouse'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(20))

    products = relationship(Product, backref='products')