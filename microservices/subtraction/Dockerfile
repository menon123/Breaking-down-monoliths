# Use an official Python runtime as a parent image
FROM python:3.9-slim-buster

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY app /app

# Install the required packages
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port
EXPOSE 5050

# Define environment variable
ENV NAME Subtraction

# Run the command to start the Flask server
CMD ["python", "app.py"]
