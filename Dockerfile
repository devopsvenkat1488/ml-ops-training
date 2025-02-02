# Use a lightweight Python base image
FROM python:3.8-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the app files to the container
COPY . /app

# Install required dependencies
RUN pip install -r requirements.txt

# Expose port 5000 for Flask
EXPOSE 5000

# Command to run the Flask app
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "app:app"]

