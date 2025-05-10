# Math API

A FastAPI-based mathematical operations API with a beautiful web interface for testing and documentation.

## Features

- Basic mathematical operations (addition, subtraction, multiplication, division)
- Advanced operations (power)
- Interactive web interface for testing
- API documentation
- Ready for deployment on Render

## Local Development

1. Clone the repository
2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the application:
   ```bash
   uvicorn main:app --reload
   ```
5. Open your browser and navigate to `http://localhost:8000`

## API Endpoints

- `POST /add` - Add two numbers
- `POST /subtract` - Subtract two numbers
- `POST /multiply` - Multiply two numbers
- `POST /divide` - Divide two numbers
- `POST /power` - Calculate power

## Deploying to Render

1. Create a new Web Service on Render
2. Connect your GitHub repository
3. Use the following settings:
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `uvicorn main:app --host 0.0.0.0 --port $PORT`
4. Deploy!

## API Documentation

The API documentation is available at the root URL (`/`) when you run the application. It provides:

- Interactive testing interface
- Endpoint descriptions
- Request/response format examples
- Error handling information

## Error Handling

The API includes proper error handling for:

- Division by zero
- Invalid input numbers
- Invalid logarithm inputs

## Technologies Used

- FastAPI
- Uvicorn
- Jinja2
- TailwindCSS
- JavaScript (Fetch API)
