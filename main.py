from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
import math
import os

app = FastAPI(title="Math API", description="A simple API for mathematical operations")

# Mount static files if directory exists
if os.path.exists("static"):
    app.mount("/static", StaticFiles(directory="static"), name="static")

# Templates
templates = Jinja2Templates(directory="templates")

class Numbers(BaseModel):
    num1: float
    num2: float

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/add")
async def add(numbers: Numbers):
    return {"result": numbers.num1 + numbers.num2}

@app.post("/subtract")
async def subtract(numbers: Numbers):
    return {"result": numbers.num1 - numbers.num2}

@app.post("/multiply")
async def multiply(numbers: Numbers):
    return {"result": numbers.num1 * numbers.num2}

@app.post("/divide")
async def divide(numbers: Numbers):
    if numbers.num2 == 0:
        return {"error": "Division by zero is not allowed"}
    return {"result": numbers.num1 / numbers.num2}

@app.post("/power")
async def power(numbers: Numbers):
    return {"result": numbers.num1 ** numbers.num2}

@app.post("/logarithm")
async def logarithm(numbers: Numbers):
    if numbers.num1 <= 0 or numbers.num2 <= 0:
        return {"error": "Numbers must be positive for logarithm"}
    return {"result": math.log(numbers.num1, numbers.num2)}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000) 