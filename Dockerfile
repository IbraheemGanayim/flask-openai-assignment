# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements.txt file into the container at /app
COPY requirements.txt .

# Install the required dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container at /app
COPY . .

# Set environment variables to avoid running Flask in debug mode in production
ENV FLASK_ENV=production

# Expose port 5000 for Flask
EXPOSE 5000

# Define the command to run the application
CMD ["python", "app.py"]