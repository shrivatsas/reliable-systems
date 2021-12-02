from typing import Optional

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read():
    return "Hello World"

@app.get("/health")
def read():
    return "I am here!"

