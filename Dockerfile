# Use Python 3.11.5 image
FROM python:3.11.5-slim

# Set environment variables
ENV PYTHONUNBUFFERED=1
ENV FLASK_ENV=production

# Create and set the working directory
WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY . .

# Set the entry point for the container
CMD ["gunicorn", "-b", "0.0.0.0:5000", "app:app"]
