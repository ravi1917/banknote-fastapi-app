from fastapi import FastAPI, Request, Form
import uvicorn
import joblib
from fastapi.templating import Jinja2Templates
import pandas as pd
from pathlib import Path

app = FastAPI()

classifier = joblib.load("classifier.pkl")

BASE_DIR = Path(__file__).resolve().parent
templates = Jinja2Templates(directory=str(BASE_DIR / "templates"))


@app.get("/")
def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={
            "prediction": None
        }
    )


@app.post("/predict_ui")
def predict_ui(
    request: Request,
    variance: float = Form(...),
    skewness: float = Form(...),
    curtosis: float = Form(...),
    entropy: float = Form(...)
):
    input_data = pd.DataFrame([{
        "variance": variance,
        "skewness": skewness,
        "curtosis": curtosis,
        "entropy": entropy
    }])

    prediction = classifier.predict(input_data)

    result = "Fake BankNote" if prediction[0] == 1 else "It's an Original BankNote"

    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={
            "prediction": result
        }
    )


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)