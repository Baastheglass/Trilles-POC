import uvicorn
from fastapi import FastAPI
from cog import cogni
from pydantic import BaseModel
import requests

app = FastAPI()
cog = cogni()
class QueryRequest(BaseModel):
    query: str

@app.get("/")
async def health_check():
    return {"status": "ok"}

@app.post("/search")
async def search(request: QueryRequest):
        # Extract query from request body
        query = request.query
        if not query:
            return {"error": "Query parameter is required"}
        print(f"Received query: {query}")
        # Search functionality
        results = await cog.search(query)
        response = requests.post("http://localhost:5678/webhook-test/test", json={"text": results})
        if response.status_code == 200:
            with open("output.mp3", "wb") as f:
                f.write(response.content)
            print("Audio saved as output.mp3")
        print(response)
        return {"results": results}

if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=8000)