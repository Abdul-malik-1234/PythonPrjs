from fastapi import FastAPI

app = FastAPI(
    title="Contact Manager API",
    description="Your CLI contact manager, now as a web API!",
    version="1.0.0"
)

@app.get("/")
def read_root():
    return {"message": "Welcome to Contact Manager API!", "status": "running"}

@app.get("/contacts")
def get_contacts():
    # We'll implement this soon - returning dummy data for now
    return {"contacts": [
        {"id": 1, "name": "John Doe", "phone": "1234567890", "email": "john@example.com"},
        {"id": 2, "name": "Jane Smith", "phone": "0987654321", "email": "jane@example.com"}
    ]}

@app.get("/health")
def health_check():
    return {"status": "healthy", "service": "Contact Manager API"}