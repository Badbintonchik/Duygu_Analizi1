from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

app = FastAPI()

class TextInput(BaseModel):
    text: str

@app.post("/predict")
async def predict(input_data: TextInput):
    # This is a simple example - you would replace this with your actual sentiment analysis model
    text = input_data.text
    
    # Dummy sentiment analysis logic (replace with your actual model)
    # For demonstration purposes only
    if "iyi" in text.lower() or "güzel" in text.lower() or "harika" in text.lower():
        positive = 0.9
        negative = 0.1
    elif "kötü" in text.lower() or "berbat" in text.lower() or "nefret" in text.lower():
        positive = 0.2
        negative = 0.8
    else:
        positive = 0.5
        negative = 0.5
    
    return {
        "positive": positive,
        "negative": negative
    }

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)