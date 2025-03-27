# Use a specific Python version as the base image
FROM python:3.12.8

# Set environment variables to prevent Python from writing .pyc files
# and to set the buffer to line-mode to make the logs easier to read
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements.txt to the container
COPY requirements.txt /app/

# Install the Python dependencies from requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your application files into the container
COPY . /app/

# Expose the Flask port
EXPOSE 5000

# Set the command to run your application using Flask
CMD ["python", "app.py"]
