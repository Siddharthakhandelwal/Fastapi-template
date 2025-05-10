from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field
from typing import List, Optional
import logging
from datetime import datetime
import uvicorn

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="Pet Store API",
    description="A FastAPI implementation of the Swagger Pet Store API",
    version="1.0.0"
)

# In-memory storage
pets_db = {}
pet_id_counter = 1

class Category(BaseModel):
    id: Optional[int] = None
    name: str

class Tag(BaseModel):
    id: Optional[int] = None
    name: str

class Pet(BaseModel):
    id: Optional[int] = None
    category: Optional[Category] = None
    name: str
    photo_urls: List[str] = []
    tags: Optional[List[Tag]] = None
    status: str = Field(..., description="pet status in the store", enum=["available", "pending", "sold"])

@app.get("/pets", response_model=List[Pet])
async def get_pets(status: Optional[str] = None):
    """Get all pets, optionally filtered by status"""
    logger.info(f"Getting pets with status filter: {status}")
    if status:
        return [pet for pet in pets_db.values() if pet.status == status]
    return list(pets_db.values())

@app.get("/pets/{pet_id}", response_model=Pet)
async def get_pet(pet_id: int):
    """Get a specific pet by ID"""
    logger.info(f"Getting pet with ID: {pet_id}")
    if pet_id not in pets_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Pet not found"
        )
    return pets_db[pet_id]

@app.post("/pets", response_model=Pet, status_code=status.HTTP_201_CREATED)
async def create_pet(pet: Pet):
    """Create a new pet"""
    global pet_id_counter
    logger.info(f"Creating new pet: {pet.name}")
    pet.id = pet_id_counter
    pets_db[pet_id_counter] = pet
    pet_id_counter += 1
    return pet

@app.put("/pets/{pet_id}", response_model=Pet)
async def update_pet(pet_id: int, pet: Pet):
    """Update an existing pet"""
    logger.info(f"Updating pet with ID: {pet_id}")
    if pet_id not in pets_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Pet not found"
        )
    pet.id = pet_id
    pets_db[pet_id] = pet
    return pet

@app.delete("/pets/{pet_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_pet(pet_id: int):
    """Delete a pet"""
    logger.info(f"Deleting pet with ID: {pet_id}")
    if pet_id not in pets_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Pet not found"
        )
    del pets_db[pet_id]

@app.middleware("http")
async def log_requests(request, call_next):
    """Middleware to log all requests and responses"""
    start_time = datetime.now()
    response = await call_next(request)
    duration = datetime.now() - start_time
    logger.info(f"{request.method} {request.url.path} - Status: {response.status_code} - Duration: {duration}")
    return response

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000) 