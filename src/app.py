import uvicorn
from fastapi import FastAPI

app = FastAPI()

if __name__ == "__main__":
    config = uvicorn.Config(
        "app:app", port=5000, log_level="info", reload=True
    )
    server = uvicorn.Server(config)
    server.run()


@app.get("/")
def home():
    return {"message": "Welcome to the Home Page!"}
