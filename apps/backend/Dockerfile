# Use Python 3.13.2 slim for Django
FROM python:3.13.2-slim

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy Django project code
COPY . .

EXPOSE 8000

# Start Django using uvicorn ASGI server
CMD ["uvicorn", "backend.asgi:application", "--host", "0.0.0.0", "--port", "8000"]
