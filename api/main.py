from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Bank-Trans API работает!"}

@app.get("/transactions")
def get_transactions():
    return [
        {"id": 1, "amount": 100.0, "from": "МАДИНА", "to": "МИРОН", "category": "еда", "date": "2025-07-15"},
        {"id": 2, "amount": 200.0, "from": "ДМИТРИЙ", "to": "КИРИЛЛ", "category": "транспорт", "date": "2025-07-14"}
    ]