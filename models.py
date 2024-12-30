# models.py
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "mysql+mysqlconnector://root:MahitNahi%4012@localhost/data_project"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class CsvData(Base):
    __tablename__ = "csv_data"
    id = Column(Integer, primary_key=True, index=True)
    column_a = Column(String)
    column_b = Column(String)
    column_c = Column(String)
    
    

Base.metadata.create_all(bind=engine)
