# Base Image
FROM python:3.12

# Set the working directory
WORKDIR /app

# Copy the requirements file
COPY requirements.txt .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Update requirements
RUN apt update && apt upgrade -y

# Install requirements
RUN apt install git -y

# Copy the application code
COPY . .

# Expose the port
EXPOSE 8080

# Command to run the application
CMD ["uvicorn", "product_pipeline:app", "--host", "localhost", "--port", "8080"]