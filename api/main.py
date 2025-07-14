from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Bank-Trans API работает!"}

@app.get("/transactions")
def get_transactions():
    return [
        {"id": 1, "amount": 100.0, "sender": "МАДИНА", "receiver": "МИРОН"},
        {"id": 2, "amount": 200.0, "sender": "ДМИТРИЙ", "receiver": "КИРИЛЛ"},
    ]