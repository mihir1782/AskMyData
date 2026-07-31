from fastapi import FastAPI
# Create my API application.
app = FastAPI()


@app.get("/")
def home():
    return {"message": "Welcome to AskMyData API!"}

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    return {"message": "Welcome to AskMyData API!"}


@app.post("/chat")
def chat():
    return {
        "question": "Show top 5 customers",
        "sql": "SELECT * FROM customers LIMIT 5;",
        "answer": "Here are the first five customers."
}

