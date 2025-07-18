from fastapi import FastAPI, Request
from logger import logger

app = FastAPI()

@app.middleware("http")
async def log_requests(request: Request, call_next):
    logger.info(f"➡️ {request.method} {request.url}")
    response = await call_next(request)
    logger.info(f"⬅️ {response.status_code} {request.url}")
    return response

@app.get("/")
def root():
    logger.info(" Вызван /")
    return {"message": "Bank-Trans API работает!"}

@app.get("/transactions")
def get_transactions():
    logger.info(" Вызван /transactions")
    return [
        {"id": 1, "amount": 100.0, "from": "МАДИНА", "to": "МИРОН", "category": "еда", "date": "2025-07-15"},
        {"id": 2, "amount": 200.0, "from": "ДМИТРИЙ", "to": "КИРИЛЛ", "category": "транспорт", "date": "2025-07-14"}
    ]