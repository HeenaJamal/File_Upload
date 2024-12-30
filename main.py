# main.py
from fastapi import FastAPI, File, UploadFile, Depends, HTTPException
from sqlalchemy.orm import Session
import pandas as pd
from typing import List
from models import CsvData, SessionLocal  # replace 'your_module' with the module name

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/upload-csv/")
async def upload_csv(file: UploadFile = File(...), db: Session = Depends(get_db)):
    if not file.filename.endswith('.csv'):
        raise HTTPException(status_code=400, detail="Only CSV files are allowed.")

    # Read the file content into a pandas DataFrame
    df = pd.read_csv(file.file)

    # Map columns to model fields
    for _, row in df.iterrows():
        csv_data = CsvData(
            column_a=row.get("A", None),
            column_b=row.get("B", None),
            column_c=row.get("C", None),
            # Map all required columns up to V
            
        )
        db.add(csv_data)

    db.commit()
    return {"status": "CSV file uploaded and data stored in database"}

@app.get("/test")
def test_endpoint():
    return {"message": "Test endpoint is working"}













































'''from fastapi import FastAPI, File, UploadFile, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models import CSVData
#from fastapi import Security
from fastapi.security import HTTPBasic, HTTPBasicCredentials
import csv
import io

app = FastAPI()

# Dependency to check if the user is an admin


def get_current_admin_user():
    user_role = "admin"  # Hardcoded for simplicity; replace with actual admin check logic
    if user_role != "admin":
        raise HTTPException(status_code=403, detail="Only admin can upload data")
    return user_role  ''

security = HTTPBasic()

def get_current_admin_user(credentials: HTTPBasicCredentials = Depends(security)):
    if credentials.username != "admin" or credentials.password != "hello12":
        raise HTTPException(status_code=403, detail="Only admin can upload data")
    return credentials.username



@app.post("/upload_csv/")
async def upload_csv(file: UploadFile = File(...), db: Session = Depends(get_db), admin_user: str = Depends(get_current_admin_user)):
    # Ensure file is a CSV
    if file.content_type != 'text/csv':
        raise HTTPException(status_code=400, detail="Invalid file format. Please upload a CSV file.")

    # Read CSV data
    contents = await file.read()
    csv_reader = csv.DictReader(io.StringIO(contents.decode('utf-8')))
    
    for row in csv_reader:
        csv_data = CSVData(
            A=row.get('A'),
            B=row.get('B'),
            C=row.get('C'),
            D=row.get('D'),
            E=row.get('E'),
            F=row.get('F'),
            G=row.get('G'),
            H=row.get('H'),
            I=row.get('I'),
            J=row.get('J'),
            K=row.get('K'),
            L=row.get('L'),
            M=row.get('M'),
            N=row.get('N'),
            O=row.get('O'),
            P=row.get('P'),
            Q=row.get('Q'),
            R=row.get('R'),
            S=row.get('S'),
            T=row.get('T'),
            U=row.get('U'),
            V=row.get('V')
        )
        db.add(csv_data)
    
    db.commit()
    return {"message": "CSV data uploaded successfully."} '''
