from fastapi import FastAPI, HTTPException
import requests

app = FastAPI()

OLLAMA_API_URL = "http://localhost:11434/api/generate"  # Ollama's default local API

@app.post("/chat")
async def chat(message: dict):
    try:
        response = requests.post(OLLAMA_API_URL, json={
            "model": "mistral",  # Change model if needed
            "prompt": message["message"],
            "stream": False
        })
        response_data = response.json()
        return {"reply": response_data.get("response", "Sorry, I can't generate a response.")}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
