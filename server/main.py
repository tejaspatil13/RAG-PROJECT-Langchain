
from fastapi import FastAPI

app = FastAPI(title="RAG-PROJECT")

@app.get("/test")
def test():
    data = {
        "name" : "tejas",
        "age" : 22
    }
    print(data)
