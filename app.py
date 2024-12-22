import os
import json
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from src.model_loader import load_vllm_model
from src.entity_extraction import extract_entities
from src.prompts import TRAVEL_PROMPT, UTILITY_PROMPT, FUEL_PROMPT

import logging

# Initialize FastAPI and load model
app = FastAPI(title="vLLM Entity Extraction API")

model = load_vllm_model()

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

        
# Request Body Schema
class TextRequest(BaseModel):
    text: str


@app.post("/extract-travel")
def extract_travel_entities(request: TextRequest):
    """
    Extract entities from travel itinerary text.
    """
    try:
        result = extract_entities(model, request.text, TRAVEL_PROMPT)
        return {"extracted_data": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/extract-utility")
def extract_utility_entities(request: TextRequest):
    """
    Extract entities from utility bill text.
    """
    try:
        result = extract_entities(model, request.text, UTILITY_PROMPT)
        return {"extracted_data": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/extract-fuel")
def extract_fuel_entities(request: TextRequest):
    """
    Extract entities from fuel bill text.
    """
    try:
        result = extract_entities(model, request.text, FUEL_PROMPT)
        return {"extracted_data": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))



@app.get("/")
def root():
    return {"message": "Welcome to the vLLM Entity Extraction API"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001)
