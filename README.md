# FastAPI Pet Store API

A FastAPI-based implementation of the Swagger Pet Store API for demonstration and testing purposes.

## Features

- CRUD operations for pets (in-memory storage)
- OpenAPI/Swagger documentation at `/docs`
- Logging of all requests and responses
- Ready for local development and cloud deployment

## Endpoints

- `POST /pets` — Create a new pet
- `GET /pets` — List all pets (optionally filter by status)
- `GET /pets/{pet_id}` — Get a pet by ID
- `PUT /pets/{pet_id}` — Update a pet by ID
- `DELETE /pets/{pet_id}` — Delete a pet by ID

## Pet Model Example

```json
{
  "name": "Fluffy",
  "category": { "name": "Dogs" },
  "photo_urls": ["http://example.com/fluffy.jpg"],
  "tags": [{ "name": "friendly" }],
  "status": "available"
}
```

## Local Development

1. Clone the repository
2. Create a virtual environment:
   ```bash
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the application:
   ```bash
   uvicorn main:app --reload
   ```
5. Open your browser and navigate to `http://localhost:8000/docs` for the Swagger UI.

## Deployment

You can deploy this app to any cloud provider that supports Python and FastAPI (e.g., Render, Heroku, Azure, etc.).

- **Build Command:** `pip install -r requirements.txt`
- **Start Command:** `uvicorn main:app --host 0.0.0.0 --port $PORT`

## License

MIT
