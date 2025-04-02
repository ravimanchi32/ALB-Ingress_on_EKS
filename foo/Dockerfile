FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the application code
COPY app.py .

# Install dependencies
RUN pip install flask

# Set environment variable
ENV PORT=8080

# Command to run the application
CMD ["python", "app.py"]
