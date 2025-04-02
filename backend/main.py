from fastapi import FastAPI

app = FastAPI(
    title = "Library Management System",
    description = "A simple library management system API built with FastAPI."
)

@app.get("/")
def root():
    return {"message": "Welcome to the Library Management System API!"}
